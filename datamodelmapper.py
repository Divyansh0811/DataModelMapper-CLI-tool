import click
import pandas as pd

class DataModelMapper():
  def __init__(self, csv_file, model):
    self.csv_file = csv_file
    self.model = model

  def createDataModel(self):
    click.echo(f"Creating data set for the model: {self.model}")
    df = pd.read_csv(self.csv_file)
    click.echo("Input Dataframe")
    click.echo(df)