from .iedb import Normalizer, IEDBDataset


datasets = {
    'IEDBDataset': IEDBDataset,
}


def get_dataset(config):
    f = datasets.get(config.name)

    return f(**config.params)
