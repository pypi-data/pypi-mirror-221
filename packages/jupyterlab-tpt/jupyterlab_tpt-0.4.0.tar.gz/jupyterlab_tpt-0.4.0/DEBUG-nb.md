# helpers

# v0 - with jtext

```bash
conda deactivate ; conda env remove -n jlab4-nb7-text
conda create -y -n jlab4-nb7-text python=3.11; conda activate jlab4-nb7-text; pip install jupyterlab; pip install --pre notebook; pip install pip install /Users/tparment/git/jupytext/dist/jupytext-1.15.0.dev1-py3-none-any.whl
pip show notebook | grep Version
```

notebook OK

![OK](OK-nb.png)

## adding myst

```bash
pip install jupyterlab-myst
```

notebook KO

![KO](KO-nb.png)

---

# v1 - separately

let's keep it simpler

```bash
conda deactivate ; conda env remove -n jlab4-nb7
conda create -y -n jlab4-nb7 python=3.11; conda activate jlab4-nb7; pip install --pre notebook
pip show notebook | grep Version
```

notebook OK

![OK](OK-nb1.png)

## adding myst

```bash
pip install jupyterlab-myst
```

notebook OK

![KO](OK-nb1.png)

## adding jtext

```bash
pip install /Users/tparment/git/jupytext/dist/jupytext-1.15.0.dev1-py3-none-any.whl
```

notebook still OK !?!

# jupytext released

