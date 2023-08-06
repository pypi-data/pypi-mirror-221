from hivecore.constant import PANDAS_TYPES, PYSPARK_TYPES, KOALAS_TYPES, PANDAS_ON_SPARK_TYPES, PANDAS, KOALAS, SPARK, PYSPARK, PANDAS_ON_SPARK, IN_PANDAS_ON_SPARK
from hiveadb.function import get_spark, get_dbutils, data_convert, to_list, df_type

spark   = get_spark()
dbutils = get_dbutils()

from numpy import median as _median
from scipy.stats import mode as _mode

# Pandas
from pandas import DataFrame, concat, to_numeric

# Pyspark.Pandas
from pyspark.pandas import DataFrame as ps_DataFrame, from_pandas as ps_from_pandas

# Pyspark
from pyspark.sql import Window
from pyspark.sql.types import StringType

# Koalas
from databricks.koalas import from_pandas, DataFrame as KoalasDataFrame

from typing import List, Union
from os import system
from pyspark.sql.functions import abs as sabs, max as smax, min as smin, mean as _mean, stddev as _stddev, count as scount, first, last
from sklearn.metrics.pairwise import cosine_similarity as sk_cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from pandas import DataFrame, concat
from typing import List, Union

import pandas
import pyspark
import databricks.koalas


from textdistance import cosine, jaro, levenshtein, damerau_levenshtein, hamming
from jellyfish import jaro_winkler
from typing import Union, List, Mapping
from pandas import DataFrame as PandasDataFrame, Series as PandasSeries, concat as PandasConcat
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql.functions import expr
from pyspark.sql.types import DoubleType
from polars import DataFrame as PolarsDataFrame, Series as PolarsSeries, Float64 as PolarsFloat64

##### NUMERIC FUNCTIONS #####
def normalize(df: Union[pandas.DataFrame, databricks.koalas.DataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame], 
              columns: List[str] = None, 
              method: str = "max-abs", 
              overwrite: bool = False) -> Union[pandas.DataFrame, databricks.koalas.DataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame]:
    """
    Normalize the values in the specified columns of a DataFrame using a given normalization method.

    :param df: A DataFrame object to normalize.
    :type df: Union[pandas.DataFrame, databricks.koalas.DataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame]

    :param columns: A list of column names to normalize. If None, normalize all columns.
    :type columns: List[str]

    :param method: The normalization method to use. Default is "max-abs".
    :type method: str

    :param overwrite: If True, overwrite the original values in the DataFrame with the normalized values.
    :type overwrite: bool

    :return: A DataFrame object with the normalized values. If overwrite is True, return the same DataFrame object.
    :rtype: Union[pandas.DataFrame, databricks.koalas.DataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame]
    """
    engine = df_type(df)
    method = method.lower()
    if engine == PANDAS or engine == KOALAS or engine == PANDAS_ON_SPARK:
        if not columns:
            s = df.apply(lambda s: to_numeric(s, errors='coerce').notnull().all())
            if engine == KOALAS or engine == PANDAS_ON_SPARK:
                columns = list(s[s].index.to_numpy())
            else:
                columns = list(s[s].index)
            
        if not isinstance(columns, list):
            columns = [columns]
            
        df = df.copy()

        if method in ["max_abs", "max-abs", "max abs", "maximum_absolute", "maximum-absolute","maximum absolute"]:
            for column in columns:
                if overwrite:
                    df[column] = df[column]  / df[column].abs().max()
                else:
                    df[f"{column}_norm"] = df[column]  / df[column].abs().max()
        elif method in ["min_max", "min-max", "min max"]:
            for column in columns:
                if overwrite:
                    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
                else:
                    df[f"{column}_norm"] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
        elif method in ["z-score"]:
            for column in columns:
                if overwrite:
                    df[column] = (df[column] - df[column].mean()) / df[column].std()
                else:
                    df[f"{column}_norm"] = (df[column] - df[column].mean()) / df[column].std()
    elif engine == PYSPARK:
        if not columns:
            columns = list()
            for column in df.columns:
                if df.select(column, df[column].cast("int").isNotNull().alias("Value")).select("Value").distinct().collect()[0]["Value"] == True and df.select(column, df[column].cast("int").isNotNull().alias("Value")).select("Value").distinct().count() == 1:
                    columns.append(column)
        if not isinstance(columns, list):
            columns = [columns]
        df = df.alias('copy')
        if method in ["max_abs", "max-abs", "max abs", "maximum_absolute", "maximum-absolute","maximum absolute"]:
            for column in columns:
                if overwrite:
                    df = df.withColumn(column, (df[column] / df.select(smax(sabs(df[column])).alias("abs-max")).collect()[0]["abs-max"]).alias(f"{column}_normalized"))
                else:
                    df = df.withColumn(f"{column}_norm", (df[column] / df.select(smax(sabs(df[column])).alias("abs-max")).collect()[0]["abs-max"]).alias(f"{column}_normalized"))
        elif method in ["min_max", "min-max", "min max"]:
            for column in columns:
                if overwrite:
                    df = df.withColumn(column, ( (df[column] - df.select(smin(df[column]).alias("min")).collect()[0]["min"]) / ((df.select(smax(df[column]).alias("max")).collect()[0]["max"]) - (df.select(smin(df[column]).alias("min") )).collect()[0]["min"])).alias(f"{column}_normalized"))
                else:
                    df = df.withColumn(f"{column}_norm", ( (df[column] - df.select(smin(df[column]).alias("min")).collect()[0]["min"]) / ((df.select(smax(df[column]).alias("max")).collect()[0]["max"]) - (df.select(smin(df[column]).alias("min") )).collect()[0]["min"])).alias(f"{column}_normalized"))
        elif method in ["z-score"]:
            for column in columns:
                if overwrite:
                    df = df.withColumn(column, ((df[column] - (df.select(_mean(df[column]).alias("mean")).collect()[0]["mean"])) / (df.select(_stddev(df[column]).alias("std")).collect()[0]["std"])).alias(f"{column}_normalized"))
                else:
                    df = df.withColumn(f"{column}_norm", ((df[column] - (df.select(_mean(df[column]).alias("mean")).collect()[0]["mean"])) / (df.select(_stddev(df[column]).alias("std")).collect()[0]["std"])).alias(f"{column}_normalized"))

    return df


def replace_nas(df: Union[KoalasDataFrame, pandas.DataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame],
                columns: List[str] = None, 
                method: str = "mean") -> Union[KoalasDataFrame, pandas.DataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame]:
    """
    Replace missing values (NAs) in the specified columns of a DataFrame with a specified method.

    :param df: The DataFrame to replace NAs in.
    :type df: Union[KoalasDataFrame, pandas.DataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame]

    :param columns: The list of columns to replace NAs in. If None, all columns with NAs will be replaced.
    :type columns: List[str]

    :param method: The method to use for replacing NAs. Available methods are "mean", "median", "mode", "ffill", and "bfill".
    :type method: str

    :return: The DataFrame with NAs replaced according to the specified method.
    :rtype: Union[KoalasDataFrame, pandas.DataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame]
    """
    engine = df_type(df)
    if not columns:
        if engine == KOALAS or engine == PANDAS_ON_SPARK:
            s = df.apply(lambda s: to_numeric(s, errors='coerce').notnull().all())
            columns = list(set(list(s[s].index.to_numpy())))
            df = df.copy()
        elif engine == PANDAS:
            s = df.apply(lambda s: to_numeric(s, errors='coerce').notnull().all())
            columns = list(s[s].index)
            df = df.copy()
        elif engine == PYSPARK:
            columns = df.columns
            df = df.alias("_copy")
    if method == "mean":
        if engine == KOALAS or engine == PANDAS_ON_SPARK:
            for column in df.columns:
                df[column] = df[column].fillna(df[column].mean())
        elif engine == PANDAS:
            df[columns] = df[columns].fillna(df.mean())
        elif engine == PYSPARK:
            for column in columns:
                mean = df.select(_mean(df[column]).alias("mean")).collect()[0]["mean"]
                df = df.na.fill(value=mean)
    if method == "median":
        if engine == KOALAS or engine == PANDAS_ON_SPARK:
            for column in df.columns:
                median = df[column].median()
                df[column] = df[column].fillna(value=median)
        elif engine == PANDAS:
            df[columns] = df[columns].fillna(df.median())
        elif engine == PYSPARK:
            for column in columns:
                median = _median(edf.select(column).na.drop().rdd.map(lambda r: r[0]).collect())
                df = df.na.fill(value=median)
    if method == "mode":
        if engine == KOALAS or engine == PANDAS_ON_SPARK:
            for column in df.columns:
                df[column] = df[column].fillna(df[column].mode()[0])
        elif engine == PANDAS:
            df[columns] = df[columns].fillna(df.mode())
        elif engine == PYSPARK:
            for column in columns:
                mode = (_mode(edf.select(column).na.drop().rdd.map(lambda r: r[0]).collect())[0][0]).item()
                df   = df.na.fill(value=mode)
    if method == "ffill" or method == "pad":
        if engine in IN_PANDAS_ON_SPARK:
            from pyspark.pandas import config as ps_config
            spark.conf.set('spark.sql.execution.arrow.enabled', 'true')
            ps_config.set_option('compute.ops_on_diff_frames', True)
        elif engine in KOALAS:
            from databricks.koalas import config as koalas_config
            koalas_config.set_option('compute.ops_on_diff_frames', True)
        if engine == KOALAS or engine == PANDAS_ON_SPARK or engine == PANDAS:
            for column in columns:
                df[column] = df[column].ffill()
        if engine == PYSPARK:
            for column in columns:
                w_forward = Window.partitionBy().orderBy(column).rowsBetween(Window.unboundedPreceding,Window.currentRow)
                w_backward = Window.partitionBy().orderBy(column).rowsBetween(Window.currentRow,Window.unboundedFollowing)
                df = df.withColumn(column,last(column,ignorenulls=True).over(w_forward))\
                  .withColumn(column,first(column,ignorenulls=True).over(w_backward))
    if method == "bfill" or method == "backfill":
        if engine in IN_PANDAS_ON_SPARK:
            from pyspark.pandas import config as ps_config
            spark.conf.set('spark.sql.execution.arrow.enabled', 'true')
            ps_config.set_option('compute.ops_on_diff_frames', True)
        elif engine in KOALAS:
            from databricks.koalas import config as koalas_config
            koalas_config.set_option('compute.ops_on_diff_frames', True)
        if engine == KOALAS or engine == PANDAS_ON_SPARK or engine == PANDAS:
            for column in columns:
                df[column] = data_convert(data_convert(df, as_type = PANDAS).bfill(), as_type = engine)[column]
        if engine == PYSPARK:
            for column in columns:
                w_forward = Window.partitionBy().orderBy(column).rowsBetween(Window.unboundedPreceding,Window.currentRow)
                w_backward = Window.partitionBy().orderBy(column).rowsBetween(Window.currentRow,Window.unboundedFollowing)
                df = df.withColumn(column,first(column,ignorenulls=True).over(w_backward))\
                    .withColumn(column,last(column,ignorenulls=True).over(w_forward))
    if method == "interpolate":
        if engine in IN_PANDAS_ON_SPARK:
            from pyspark.pandas import config as ps_config
            ps_config.set_option('compute.ops_on_diff_frames', True)
        elif engine in KOALAS:
            from databricks.koalas import config as koalas_config
            koalas_config.set_option('compute.ops_on_diff_frames', True)
        if engine == KOALAS:
            for column in df.columns:
                df[column] = data_convert(data_convert(df, as_type = PANDAS)[column].interpolate(), as_type = engine)
        if engine == PANDAS_ON_SPARK:
            spark.conf.set('spark.sql.execution.arrow.enabled', 'true')
            for column in df.columns:
                df[column] = data_convert(data_convert(df, as_type = PANDAS).interpolate(), as_type = engine)[column]
        elif engine == PANDAS:
            df[columns] = df[columns].interpolate()
        if engine == PYSPARK:
            # CURRENT IMPLEMENTATION IS JUST TRYING TO BRUTE FORCE A PANDAS IMPLEMENTATION, TOO LAZY TO WORK THIS AROUND.
            try:
                for column in df.columns:
                    df = df.unionByName(data_convert(data_convert(df.select(column), as_type=PANDAS).interpolate(), as_type=PYSPARK), allowMissingColumns=True)
                    df.drop(column)
                    df.withColumnRenamed(f"{column}_t", column)
            except:
                raise
    if method == "drop":
        if engine == KOALAS or engine == PANDAS_ON_SPARK or engine == PANDAS:
            df = df.dropna()
        if engine == PYSPARK:
            df = df.na.drop()
    return df


##### TEXT FUNCTIONS #####
def text_similarity(original_source, comparison_text, engine="auto", threshold=None, dict_attr='values', columns=None, new_column=True) -> Union[float, List, Mapping, PandasDataFrame, PandasSeries, SparkDataFrame, PolarsDataFrame, PolarsSeries]:
    """
    Calculate the similarity between two texts using different algorithms.

    :param original_source: The original text or column-like structure.
    :type original_source: str, list, dict, pandas.DataFrame, pandas.Series, pyspark.sql.DataFrame
    :param comparison_text: The text to compare with the original text.
    :type comparison_text: str
    :param engine: The algorithm/engine to use for similarity calculation. Defaults to "auto".
    :type engine: str, optional
    :param threshold: The similarity threshold. If specified, the result is a boolean indicating whether the similarity
                      is above or equal to the threshold. If not specified, the similarity value is returned.
    :type threshold: float, optional
    :param dict_attr: An option to specify what to use as an iterator for the similarities, "values" or "keys". Defaults to "values".
    :type dict_attr: str
    :param columns: Used to define the columns to apply the similarity to. Defaults to None.
    :type columns: List[str], optional
    :param new_column: Whether to add new columns for similarity scores or overwrite existing columns. Defaults to False.
    :type new_column: bool, optional
    :return: The DataFrame with similarity scores.
    :rtype: Union[float, List, Mapping, pandas.DataFrame, pandas.Series, pyspark.sql.DataFrame, polars.DataFrame, polars.Series]
    """

    def text_similarity_wrapper(original_source, comparison_text, engine, threshold):
        # Validate threshold if specified
        if threshold is not None and (not isinstance(threshold, float) or not 0 <= threshold <= 1):
            raise ValueError("Threshold must be a float between 0 and 1.")

        # Validate original_source type
        if not isinstance(original_source, str):
            raise ValueError(f"Original text must be a string, not type {type(original_source)}")
        
        # Validate original_source type
        if not isinstance(comparison_text, str):
            raise ValueError(f"Comparison text must be a string, not type {type(comparison_text)}")

        # Validate engine
        if engine == "auto":
            if len(original_source) > 100 or len(comparison_text) > 100:
                engine = "cosine"
            else:
                engine = "jaro"
        elif engine not in ["cosine", "jaro", "jaro_winkler", "levenshtein", "damerau_levenshtein", "hamming"]:
            raise ValueError(f"Invalid engine: {engine}")



        # Calculate similarity based on the engine
        if engine == "cosine":
            similarity = cosine.normalized_similarity(original_source, comparison_text)
        elif engine == "jaro":
            similarity = jaro.normalized_similarity(original_source, comparison_text)
        elif engine == "jaro_winkler":
            similarity = jaro_winkler(original_source, comparison_text)
        elif engine == "levenshtein":
            similarity = levenshtein.normalized_similarity(original_source, comparison_text)
        elif engine == "damerau_levenshtein":
            similarity = damerau_levenshtein.normalized_similarity(original_source, comparison_text)
        elif engine == "hamming":
            similarity = hamming.normalized_similarity(original_source, comparison_text)

        # Return similarity or boolean result based on threshold
        if threshold is None:
            return similarity
        else:
            return similarity >= threshold

    # Register the text_similarity_wrapper function as a UDF
    spark.udf.register("text_similarity_wrapper", text_similarity_wrapper, DoubleType())

    if isinstance(original_source, str):
        # RETURN THE NORMAL CALL WHEN THE TYPE IS STR
        return text_similarity_wrapper(original_source, comparison_text, engine, threshold)
    elif isinstance(original_source, list):
        # RETURN A LIST MAPPED BY THE LIST ITEMS.
        if any(unexpected_type := list(filter(None,[item if not isinstance(item, str) else None for item in original_source]))):
            raise ValueError(f"Found invalid item in list of type {', '.join(list(map(lambda item: type(item).name, unexpected_type)))}")
        
        return list(map(lambda text: text_similarity_wrapper(text, comparison_text, engine, threshold), original_source))
    elif isinstance(original_source, dict):
        # RETURNS A DICT MAPPED BY KEYS OR VALUES.
        if dict_attr.lower() == "value" or dict_attr.lower() == "values":
            iterator = original_source.items()
            return dict(map(lambda item: (item[0],text_similarity_wrapper(item[1], comparison_text, engine, threshold)), iterator))
        elif dict_attr.lower() == "key" or dict_attr.lower() == "keys":
            iterator = original_source.keys()
            return dict(map(lambda item: (item,text_similarity_wrapper(item, comparison_text, engine, threshold)), iterator))
        else:
            raise ValueError(f"Parameter dict_attr not recognized {dict_attr}")
    elif isinstance(original_source, PandasDataFrame):
        # RETURN A DATAFRAME AFTER APPLYING THE WRAPPER TO SELECTED COLUMNS.
        if columns is None:
            columns = original_source.columns.tolist()

        similarity_df = original_source[columns].applymap(
            lambda item: text_similarity_wrapper(item, comparison_text, engine, threshold)
        )

        if new_column:
            similarity_df = PandasConcat([original_source, similarity_df.add_suffix('_similarity')], axis=1)
        else:
            similarity_df.columns = original_source.columns

        return similarity_df
    elif isinstance(original_source, PandasSeries):
        # RETURN A SERIES AFTER APPLYING THE WRAPPER TO ALL THE ITEMS IN IT.
        return original_source.apply(lambda item: text_similarity_wrapper(item, comparison_text, engine, threshold))
    elif isinstance(original_source, SparkDataFrame):
        if columns is None:
            columns = original_source.columns

        similarity_exprs = []
        for col in columns:
            # Generate a new column name for similarity scores
            if new_column:
                new_col_name = col + "_similarity"
                # Check if the new column name already exists in the DataFrame
                while new_col_name in original_source.columns:
                    new_col_name += "_1"
            else:
                new_col_name = col

            # Create the expression to calculate the similarity score
            expr_col = expr("text_similarity_wrapper({}, '{}', '{}', {})".format(
                col, comparison_text, engine, "CAST({} AS DOUBLE)".format(threshold) if threshold is not None else "NULL"
            )).alias(new_col_name)

            # Append the expression to the list
            similarity_exprs.append(expr_col)

        # Select the similarity expressions along with the original columns
        # Overwrite the existing columns inplace
        if new_column:
            df = original_source.select("*", *similarity_exprs)
        else:
            df = original_source.select(*[expr_col if col in columns else col for col, expr_col in zip(original_source.columns, similarity_exprs)])

        return df
    elif isinstance(original_source, PolarsDataFrame):
        # Multiple columns case
        if columns is None:
            columns = original_source.columns

        def text_similarity_func(item):
            return text_similarity_wrapper(item, comparison_text, engine, threshold)
        
        new_columns = list()

        for column in columns:
            # Apply text_similarity to the selected column
            similarity_col = f"{column}_similarity"
            similarity = original_source[column].apply(lambda x: text_similarity_func(x), return_dtype=PolarsFloat64())
            new_columns.append(similarity.alias(similarity_col))

        if new_column:
            original_source = original_source.with_columns(new_columns)
        else:
            for column in columns:
                original_source = original_source.drop(column)
            original_source = original_source.with_columns(new_columns)

        return original_source
    elif isinstance(original_source, PolarsSeries):
        # RETURN A SERIES AFTER APPLYING THE WRAPPER TO ALL THE ITEMS IN IT.
        if columns is None:
            columns = original_source.columns
        def text_similarity_func(item):
            return text_similarity_wrapper(item, comparison_text, engine, threshold)

        return original_source.select(columns).apply(text_similarity_func)
    else:
        raise ValueError("Unsupported data type: {}".format(type(original_source)._name_))


def encode(df: Union[pandas.DataFrame, KoalasDataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame], 
           columns: List[str], 
           encoder: str = "categorical", 
           overwrite: bool = False,
           as_type: str = None) -> Union[pandas.DataFrame, KoalasDataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame]:
    """
    Encodes columns in a dataframe using various encoders.

    :param df: A Pandas, Koalas, PySpark DataFrame or PySpark Koalas DataFrame to encode.
    :type df: Union[pandas.DataFrame, KoalasDataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame]

    :param columns: The names of the columns to encode.
    :type columns: List[str]

    :param encoder: The encoding method to use, Possible values are "categorical" or "onehot". defaults to "categorical".
    :type encoder: str, optional

    :param overwrite: If True, overwrites the original columns with the encoded values, defaults to False.
    :type overwrite: bool, optional

    :param as_type: The data type to convert the encoded columns to, defaults to None.
    :type as_type: str, optional

    :return: A Pandas, Koalas, PySpark DataFrame or PySpark Koalas DataFrame with the encoded columns.
    :rtype: Union[pandas.DataFrame, KoalasDataFrame, pyspark.sql.DataFrame, pyspark.pandas.DataFrame]
    """
    if not isinstance(columns, list):
        columns = [columns]
    
    engine = df_type(df)
    original_columns = df.columns

    df = data_convert(df, engine)
        
    if encoder in ["categorical", "string"]:
        for column in columns:
            if engine == PANDAS or engine == KOALAS or engine in IN_PANDAS_ON_SPARK:
                df = df.copy()
                if engine in IN_PANDAS_ON_SPARK:
                    from pyspark.pandas import config as ps_config
                    ps_config.set_option("compute.max_rows", None)
                elif engine in KOALAS:
                    from databricks.koalas import config as koalas_config
                    koalas_config.set_option("compute.max_rows", None)
                df[column] = df[column].astype("category")
                if overwrite:
                    df[column] = df[column].cat.codes
                else:
                    df[f"{column}_encoded"] = df[column].cat.codes
            elif engine == PYSPARK:
                df = df.alias("_copy")
                from pyspark.ml.feature import StringIndexer
                from pyspark.sql.functions import col
                if overwrite:
                    df = df.withColumn(column, df[column].cast(StringType()))
                    indexer = StringIndexer(inputCol=column, outputCol=f"{column}_encoded")
                    indexer_fitted = indexer.fit(df)
                    df = indexer_fitted.transform(df).drop(column).withColumnRenamed(f"{column}_encoded", column).withColumn(column,col(column).cast("int")).select(original_columns)
                else:
                    df = df.withColumn(column, df[column].cast(StringType()))
                    indexer = StringIndexer(inputCol=column, outputCol=f'{column}_encoded')
                    indexer_fitted = indexer.fit(df)
                    df = indexer_fitted.transform(df).withColumn(f"{column}_encoded",col(f"{column}_encoded").cast("int"))
    elif encoder in ["onehot", "one-hot", "one hot"]:
        for column in columns:
            if engine == PANDAS or engine == KOALAS or engine in IN_PANDAS_ON_SPARK:
                if engine in IN_PANDAS_ON_SPARK:
                    raise NotImplementedError("Current version doesn't support this opperation for pyspark.pandas.")
                    from pyspark.pandas import config as ps_config
                    ps_config.set_option("compute.max_rows", None)
                elif engine in KOALAS:
                    raise NotImplementedError("Current version doesn't support this opperation for databricks.koalas.")
                    from databricks.koalas import config as koalas_config
                    koalas_config.set_option("compute.max_rows", None)
                df = df.copy()
                df[column] = df[column].astype("category")
                uniques = len(df["firstName"].unique()) - 1
                if overwrite:
                    df[column] = df[column].cat.codes
                    df[column] = df[column].apply(lambda category: (uniques, [category], [1.0]))
                else:
                    df[f"{column}_encoded"] = df[column].cat.codes
                    df[f"{column}_encoded"] = df[f"{column}_encoded"].apply(lambda category: (uniques, [category], [1.0]))
            if engine == PYSPARK:
                from pyspark.ml.feature import OneHotEncoder, StringIndexer
                from pyspark.sql.functions import col
                df = df.alias("_copy")
                df = df.withColumn(column, df[column].cast(StringType()))
                encoder = OneHotEncoder(inputCols=[f'{column}_encoded'], outputCols=[f'{column}_onehot'])
                indexer = StringIndexer(inputCol=column, outputCol=f'{column}_encoded')
                indexer_fitted = indexer.fit(df)
                df = indexer_fitted.transform(df).withColumn(f"{column}_encoded",col(f"{column}_encoded").cast("int"))
                df = encoder.fit(df).transform(df).drop(f'{column}_encoded')
    if as_type:
        return data_convert(df, as_type)
    else:
        return data_convert(df, engine)
