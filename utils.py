def df_astype(df, new_type):
    return df.astype(new_type)


def add_zero_left(df, col, width):
    df[col] = df[col].str.zfill(width)
    return df


def add_zero_right(df, col, width):
    df[col] = df[col].str.ljust(width, "0")
    return df


def col_upper(df, col):
    df[col] = df[col].str.upper()
    return df


def add_new_col(df, pos, col, val):
    df.insert(pos, col, val)
    return df


def col_upper_first_letter(df, col):
    df[col] = df[col].str.title()
    return df


def str_extract(df, col_source, col_target, pat):
    df[col_target] = df[col_source].str.extract(pat)
    return df


def col_replace(df, to_replace, val, col=None):
    if col:
        df[col].replace(to_replace, val, regex=True, inplace=True)
    else:
        df.replace(to_replace, val, regex=True, inplace=True)
    return df


def df_subtract_string(df, col_source, col_target):
    df[col_target] = [a.replace(b, '').strip()
                      for a, b in zip(df[col_target], df[col_source])]
    return df


def str_strip(df, col):
    df[col] = df[col].str.strip()
    return df


def drop_row(df, col):
    df = df.dropna(subset=col)
    return df


def drop_duplicates_keep_first(df):
    df = df.drop_duplicates(keep='first', inplace=False)
    return df


def drop_col(df, col):
    df = df.drop(columns=col)
    return df


def rename_col(df, dict_name):
    df = df.rename(columns=dict_name)
    return df