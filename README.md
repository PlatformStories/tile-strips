# tile-strips

A GBDX task for tiling image strips. This task accepts a directory containing GeoTiff imagery as input and uses gdal_translate to complete the tiling. This will speed up extraction of data from large imagery as in [chip-from-vrt](https://github.com/PlatformStories/chip-from-vrt). It will also expedite [adding overlays](http://www.gdal.org/gdaladdo.html).


## Run

The task will tiles all images in the input directory. The following steps walk through a sample execution of the task.

1. In an iPython terminal create a GBDX interface and specify the input location:

    ```python
    from gbdxtools import Interface()
    from os.path import join
    import uuid

    gbdx = Interface()
    input_location = 's3://gbd-customer-data/58600248-2927-4523-b44b-5fec3d278c09/platform-stories/tile-strips/'
    ```

2. Create a task instance and set the imagery input:

    ```python
    tiler = gbdx.Task('tile-strips')
    tiler.inputs.images = join(input_location, 'images')
    ```

3. Create a workflow and specify the output location:

    ```python
    # Specify output location with random string
    random_str = str(uuid.uuid4())
    output_location = join('platform-stories/trial-runs', random_str)

    tiler_wf = gbdx.Workflow([tiler])
    tiler_wf.savedata(tiler.outputs.tiled_images, join(output_location, 'tiled_images'))
    ```

4. Execute the workflow:

    ```python
    tiler_wf.execute()
    ```


## Input ports

| **Parameter:**  | Description:                                                     |
|-----------------|------------------------------------------------------------------|
| iamges | Directory: Contains a GeoTiff images to be tiled. Note that any image with a '.tif' extension will be tiled. |


## Output ports

| Name  | Type | Description:                                      |
|-------|---------|---------------------------------------------------|
| tiled_images | Directory | Tiled versions of the input images. |


## Development

### Build the Docker image

You need to install [Docker](https://docs.docker.com/engine/installation/).

Clone the repository:

```bash
git clone https://github.com/platformstories/tile-strips
```

Then:

```bash
cd tile-strips
docker build -t yourusername/tile-strips .
```

Then push the image to Docker Hub:

```bash
docker push yourusername/tile-strips
```

The image name should be the same as the image name under containerDescriptors in tile-strips.json.


### Register on GBDX

In a Python terminal:

```python
import gbdxtools
gbdx = gbdxtools.Interface()
gbdx.task_registry.register(json_filename='tile-strips.json')
```
