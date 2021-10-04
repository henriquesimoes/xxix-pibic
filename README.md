# An Exploratory Analysis of Linear Epitopes and Associated Antibody CDRs in the IEDB

Here are source codes used in the analysis made in the paper "An Exploratory
Analysis of Linear Epitopes and Associated Antibody Complementarity-Determining
Regions in the Immune Epitope Database", presented in the [_XXIX Congresso de
Iniciação Científica da Unicamp_][xxix-pibic] (XXIX Unicamp's Scientific
Initiation Congress).

## Repository Structure

A walkthrough on the analysis and charts shown in the paper can be found in the
[`analysis.ipynb`](./analysis.ipynb) file. In order to make the notebook code a
bit cleaner, auxiliary Python scripts have been used and can be found in the
[`util`](./util) folder.

## How to run

Before you can run, you simply need to have [Jupyter][jupyter] configured in the
machine you are willing to (re)execute the notebook cells. Please, refer to the
[Jupyter installation guide][jupyter-install] for a step-by-step guide.

Moreover, you will need to install the package dependencies listed in
[`requirements.txt`](./requirements.txt). For doing so, use

```bash
pip install -r requirements.txt
```

After that, you just need to launch JupyterLab (or Jupyter Notebook) on the
cloned repository folder. For instance, you may use

```bash
git clone https://github.com/henriquesimoes/xxix-pibic repo
jupyterlab repo
```

and open the [analysis.ipynb](./analysis.ipynb) file through the software visual
interface.

[jupyter]: https://jupyter.org/
[jupyter-install]: https://jupyter.org/install

## Acknowledgments

We thank [FAPESP][fapesp] for financially supporting the project under grand
\#2020/11194-4 and [SAE/Unicamp][sae-unicamp] for financially supporting Henrique
F. Simões.

Opinions, hypothesis and conclusions, or recommendations made in this material
are responsibility of the author, and do not necessarily reflect FAPESP's point
of view.

[simoes]: http://lattes.cnpq.br/2364440352119569
[meidanis]: http://lattes.cnpq.br/1313385414995585

[fapesp]: https://fapesp.br/en/
[sae-unicamp]: https://www.sae.unicamp.br
[xxix-pibic]: https://www.prp.unicamp.br/pibic/congressos/xxixcongresso
