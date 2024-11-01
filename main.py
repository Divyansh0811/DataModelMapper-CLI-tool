import click
import pandas as pd
from datamodelmapper import DataModelMapper
@click.group()
def cli():
  """DataModelMapper CLI for converting CSV datasets"""
  pass


@cli.command(name='create')
@click.argument('csv_file', type=click.Path(exists=True))
@click.option('--model', type=click.Choice(['openai-gpt', 'google-bert', 'meta-llama'], case_sensitive=False), required=True, help='Select the Model type for conversion')
def create(csv_file, model):
  data_model_mapper = DataModelMapper(csv_file, model)
  data_model_mapper.createDataModel()
