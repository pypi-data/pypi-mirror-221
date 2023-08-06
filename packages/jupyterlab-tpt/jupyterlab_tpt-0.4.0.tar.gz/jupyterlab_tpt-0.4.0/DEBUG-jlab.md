# v0 - the target

```bash
grep -v '^ *$' requirements.txt
# tooling
jupyterlab
notebook
# not yet released
/Users/tparment/git/jupytext/dist/jupytext-1.15.0.dev1-py3-none-any.whl
# not yet stable
jupyterlab-myst
# not installing this at once,
# and installing afterwards, seems to work better
jupyterlab-courselevels
# for vs-code
ipykernel
# contents
ipympl
matplotlib
ipywidgets >= 8.0
# for examples
sphinxcontrib_mermaid
ipythontutor
nbautoeval
```

![KO](./KO.png)

# incremental (1)

```bash
grep -v '^ *$' requirements.txt
# tooling
jupyterlab
notebook
# not yet released
/Users/tparment/git/jupytext/dist/jupytext-1.15.0.dev1-py3-none-any.whl
# not yet stable
jupyterlab-myst
# not installing this at once,
# and installing afterwards, seems to work better
# jupyterlab-courselevels
# for vs-code
ipykernel
# contents
ipympl
matplotlib
ipywidgets >= 8.0
# for examples
sphinxcontrib_mermaid
ipythontutor
nbautoeval
```

result = OK

![OK](./OK.png)

# incremental (2)

after the previous experiment, I manually install

`pip install jupyterlab-courselevels`

result = OK

# v2 - put it last

all in `requirements.txt`, but the suspicious module comes last

result = OK !?!

# v3 - stop after the culprit

putting back the module at its place, and comment out the ones after it

OK

# v4 - the first half

re-adding the first half after the suspicious module

```bash
grep -v '^ *$' requirements.txt
# tooling
jupyterlab
notebook
# not yet released
/Users/tparment/git/jupytext/dist/jupytext-1.15.0.dev1-py3-none-any.whl
# not yet stable
jupyterlab-myst
# not installing this at once,
# and installing afterwards, seems to work better
jupyterlab-courselevels
# for vs-code
ipykernel
# contents
ipympl
matplotlib
ipywidgets >= 8.0
# # for examples
# sphinxcontrib_mermaid
# ipythontutor
# nbautoeval
```

result = OK

# v5 - the second half

enable the other half of the trailing modules

```bash
grep -v '^ *$' requirements.txt
# tooling
jupyterlab
notebook
# not yet released
/Users/tparment/git/jupytext/dist/jupytext-1.15.0.dev1-py3-none-any.whl
# not yet stable
jupyterlab-myst
# not installing this at once,
# and installing afterwards, seems to work better
jupyterlab-courselevels
# # for vs-code
# ipykernel
# # contents
# ipympl
# matplotlib
# ipywidgets >= 8.0
# for examples
sphinxcontrib_mermaid
ipythontutor
nbautoeval
```

result = OK !?!

# v6 - adding the 3 last modules one by one

## sphinxcontrib_mermaid

```bash
# tooling
jupyterlab
notebook
# not yet released
/Users/tparment/git/jupytext/dist/jupytext-1.15.0.dev1-py3-none-any.whl
# not yet stable
jupyterlab-myst
# not installing this at once,
# and installing afterwards, seems to work better
jupyterlab-courselevels
# # for vs-code
# ipykernel
# contents
ipympl
matplotlib
ipywidgets >= 8.0
# # for examples
sphinxcontrib_mermaid
# ipythontutor
# nbautoeval
```

result = OK

## ipythontutor

```bash
grep -v '^ *$' requirements.txt
# tooling
jupyterlab
notebook
# not yet released
/Users/tparment/git/jupytext/dist/jupytext-1.15.0.dev1-py3-none-any.whl
# not yet stable
jupyterlab-myst
# not installing this at once,
# and installing afterwards, seems to work better
jupyterlab-courselevels
# # for vs-code
# ipykernel
# contents
ipympl
matplotlib
ipywidgets >= 8.0
# # for examples
sphinxcontrib_mermaid
ipythontutor
# nbautoeval
```

result = OK

## nbautoeval

```bash
grep -v '^ *$' requirements.txt
# tooling
jupyterlab
notebook
# not yet released
/Users/tparment/git/jupytext/dist/jupytext-1.15.0.dev1-py3-none-any.whl
# not yet stable
jupyterlab-myst
# not installing this at once,
# and installing afterwards, seems to work better
jupyterlab-courselevels
# # for vs-code
# ipykernel
# contents
ipympl
matplotlib
ipywidgets >= 8.0
# for examples
sphinxcontrib_mermaid
ipythontutor
nbautoeval
```

result = OK

# conclusion

turns out that I forgot to re-inject `ipykernel`,
which indeed seems to be another culprit

given that it was injected only for the sake of vs-code, we'll keep it out of
the picture for now

# last experiment

## = reinjecting `ipykernel` at the end

```bash
grep -v '^ *$' requirements.txt
# tooling
jupyterlab
notebook
# not yet released
/Users/tparment/git/jupytext/dist/jupytext-1.15.0.dev1-py3-none-any.whl
# not yet stable
jupyterlab-myst
# not installing this at once,
# and installing afterwards, seems to work better
jupyterlab-courselevels
# contents
ipympl
matplotlib
ipywidgets >= 8.0
# for examples
sphinxcontrib_mermaid
ipythontutor
nbautoeval
# would be useful for vs-code but creates some trouble
# as jupyterlab looses its tool, so let's keep it out for now
ipykernel
```

result = KO

## same in 2 passes

install everything except `ipykernel` from `requirements.txt`, 
then install `ipykernel` separately

result = OK
