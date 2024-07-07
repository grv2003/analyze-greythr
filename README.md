# analyze-greythr

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) of Matatika datasets for `tap-greythr`. These datasets are automatically added to your Matatika workspace when you initialize a `tap-greythr` pipeline.

Files:

- [`analyze/datasets`](./bundle/analyze/datasets) (directory)

### Adding this file bundle to your own Meltano project

Add plugin to `discovery.yml`:

```yaml
files:
  - name: analyze-greythr
    namespace: tap_greythr
    repo: https://github.com/grv2003/analyze-greythr.git
    pip_url: git+https://github.com/grv2003/analyze-greythr.git
```

Add plugin to your Meltano project:

```bash
# Add only the file bundle
meltano add files analyze-greythr

# Add the file bundle as a related plugin through adding the extractor
meltano add extractor --include-related tap-greythr
```

### Adding this along with tap-greythr as a custom plug-in for in Matatika

Go to data imports, click on `Custom Data Source` and copy and paste in:

```yaml
extractors:
  - name: tap-greythr
    namespace: tap_greythr
    pip_url: git+https://github.com/grv2003/tap-greythr.git
    capabilities:
      - state
      - discover
      - catalog
    settings:
      - name: example_setting_one
        kind: password
      - name: example_setting_two
files:
  - name: analyze-greythr
    namespace: tap_greythr
    update:
      analyze/datasets/tap-greythr: true
    pip_url: git+https://github.com/grv2003/analyze-greythr.git
```
