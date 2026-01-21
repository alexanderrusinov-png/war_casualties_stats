import pandas as pd
import glob
import os

from src.initial_values import  SERVER_SOURCES_DIR

alldata = pd.DataFrame(columns=["gender", "age", "territory", "source"])

# Rename known variations
# Column mapping

column_map = {
    "sex": "gender",
    "years": "age",
    "country": "territory",
    "state": "territory",
    "nation": "territory",
    "location": "territory",
}


def return_all_countries():
    countries = alldata["country"].unique()
    return countries

def rows_counts_by_source():
    rows_counts = alldata.groupby("source").size()
    return rows_counts

def load_result(source, status, filename, error):
    return {
        "src_description": source,
        "status": status,
        "file": filename,
        "error": error,
    }

def process_loaded_source(src_description, df, territory, details):
    errors = ""

    # Normalize column names
    df.columns = [col.strip().lower() for col in df.columns]

    df = df.rename(columns=column_map)

    if "territory" in df.columns:
        # Use the territory values from the file
        pass
    else:
        # Add territory name provided as parameter or inferred territory from filename
        if territory is not None:
            df["territory"] = territory

    # Required columns
    required = ["gender", "age", "territory"]

    for col in required:
        if col not in df.columns:
            errors += f"Missing required column: {col}"

    if errors != "":
        return errors

    # Extract only the needed columns
    df_small = df[required].copy()

    full_src = src_description
    if details is not None:
        full_src = src_description + ":" + details

    # Add source column
    df_small["source"] = full_src

    global alldata
    print("df_small shape:", df_small.shape)
    print("alldata shape:", alldata.shape)

    alldata = pd.concat([alldata, df_small], ignore_index=True)
    print("new alldata shape:", alldata.shape)

    return ""


def load_csv_file(src_description, filedir, filename, src_details = None, territory=None):
    """
    Load a CSV file and tag it with a country name.
    """
    full_path = os.path.join(filedir, filename)
    print("full_path:", full_path, ",filename", filename)

    if not os.path.exists(full_path):
        return load_result(src_description, "error", filename, f"File not found: {filename}")

    try:
        df = pd.read_csv(full_path)
    except Exception as e:
        return load_result(src_description, "error", filename, f"Error loading CSV file '{filename}': {e}")

    inferred_territory = territory
    if inferred_territory is None:
        base = os.path.basename(filename)
        name_without_ext = os.path.splitext(base)[0]
        # Split on "_" and take the first part
        inferred_territory = name_without_ext.split("_")[0]

    # source_name = os.path.basename(filename)
    err = process_loaded_source(src_description, df, inferred_territory, src_details)

    if err == "":
        return load_result(src_description, "success", filename, "OK")

    return load_result(src_description, "error", filename, err)

def make_description(src):
    return src["type"]+":"+src["value"]

def load_server_file(src):
    filedir = SERVER_SOURCES_DIR
    filename = src["value"]

    src_description = make_description(src)
    return [load_csv_file(src_description, filedir, filename )]


def load_server_dir(src):
    basedir = SERVER_SOURCES_DIR
    dirname = src["value"]
    src_description = make_description(src)

    folder_path = os.path.join(basedir, dirname)

    print("load folder: ", folder_path)
    pattern = os.path.join(folder_path, "*.csv")
    files = glob.glob(pattern)

    if not files:
        return [load_result(src_description, "error", "", f"No CSV files found in: {folder_path}")]

    result = []
    for file in files:
        result.append(load_csv_file(src_description, folder_path, os.path.basename(file), os.path.basename(file)))

    return result

def load_url_file (src):
    url_link = src["value"]
    src_description = make_description(src)

    try:
        df = pd.read_csv(url_link)
    except Exception as e:
        return load_result(src_description, "error", url_link, f"Error loading CSV from URL '{url_link}': {e}")

    return process_loaded_source(src_description, df, None, None)

def clean_storage():
    global alldata
    alldata = pd.DataFrame(columns=["gender", "age", "territory", "source"])

def load_sources(sources):
    results = []

    for src in sources:

        if src["type"] == "server-file":
            result = load_server_file(src)

        elif src["type"] == "server-dir":
            result = load_server_dir(src)

        #if src["type"] == "local":
        #    result = load_local_file(src)

        elif src["type"] == "url":
            result =  load_url_file(src)
        else:
            result = [load_result(make_description(src), "error", "", f"Unknown source type: {src["type"]}")]

        results.extend(result)

    return results