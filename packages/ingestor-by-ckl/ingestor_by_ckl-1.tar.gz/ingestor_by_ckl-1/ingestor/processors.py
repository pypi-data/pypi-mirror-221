from pyspark.ml import Transformer
import pyspark.sql.functions as F
from pyspark import keyword_only
from pyspark.ml.param.shared import HasInputCols, HasOutputCol, HasInputCol
from pyspark.ml.util import DefaultParamsReadable, DefaultParamsWritable

class PreProcessor(Transformer, HasOutputCol, HasInputCols, DefaultParamsReadable, DefaultParamsWritable):
    @keyword_only
    def __init__(self, inputCols=None, outputCol=None):
        super(PreProcessor, self).__init__()
        kwargs = self._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, inputCols=None, outputCol=None):
        kwargs = self._input_kwargs
        return self._set(**kwargs)
    
    def setInputCols(self, value):
        """
        Sets the value of :py:attr:`inputCol`.
        """
        return self._set(inputCols=value)

    def setOutputCol(self, value):
        """
        Sets the value of :py:attr:`outputCol`.
        """
        return self._set(outputCol=value)

    def _transform(self, dataset):
        output_column = self.getOutputCol()
        input_columns = self.getInputCols()
        return (
            dataset
            .withColumn(output_column, F.col(input_columns[0]) * F.col(input_columns[1]))
        )

class PostProcessor(Transformer, HasOutputCol, HasInputCol, DefaultParamsReadable, DefaultParamsWritable):
    @keyword_only
    def __init__(self, inputCol=None, outputCol=None):
        super(PostProcessor, self).__init__()
        kwargs = self._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, inputCol=None, outputCol=None):
        kwargs = self._input_kwargs
        return self._set(**kwargs)
    
    def setInputCol(self, value):
        """
        Sets the value of :py:attr:`inputCol`.
        """
        return self._set(inputCol=value)

    def setOutputCol(self, value):
        """
        Sets the value of :py:attr:`outputCol`.
        """
        return self._set(outputCol=value)

    def _transform(self, dataset):
        output_column = self.getOutputCol()
        input_column = self.getInputCol()
        # Clip regression values at a minimum of 0.
        return dataset.withColumn(output_column, F.when(F.col(input_column) < 0.0,0.0).otherwise(F.col(input_column)))