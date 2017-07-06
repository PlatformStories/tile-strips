# tile-strips

A GBDX task for tiling images using gdal_translate. Tiling speeds up pixel extraction from large image files as in [chip-from-vrt](https://github.com/PlatformStories/chip-from-vrt) and expedites [adding overlays](http://www.gdal.org/gdaladdo.html).


## Run

The task tiles all the images found in the input directory. 
Here are the steps for a sample execution of the task.

1. In an Python terminal create a GBDX interface and specify the input location:

    ```python
    from gbdxtools import Interface
    from os.path import join
    import uuid

    gbdx = Interface()
    input_location = 's3://gbd-customer-data/32cbab7a-4307-40c8-bb31-e2de32f940c2/platform-stories/tile-strips/'
    ```

2. Create a task instance and set the imagery input:

    ```python
    tiler = gbdx.Task('tile-strips')
    tiler.inputs.images = join(input_location, 'images')
    ```

3. Create a workflow and specify the output location:

    ```python
    output_location = 'platform-stories/trial-runs/tiled-images'

    tiler_wf = gbdx.Workflow([tiler])
    tiler_wf.savedata(tiler.outputs.tiled_images, output_location)
    ```

4. Execute the workflow:

    ```python
    tiler_wf.execute()
    ```


## Input ports

| Name | Type | Description | Required |
|-----------------|--------------|--------------|--------------|
| images | Directory | Contains images to be tiled. All images with a '.tif' extension will be tiled. | True |


## Output ports

| Name  | Type | Description:                                     |
|-------|---------|---------------------------------------------------|
| tiled_images | Directory | Contains tiled input images. |


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
