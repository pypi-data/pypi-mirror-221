# RLSMorph
***Here Should Be a Logo***

[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![build](https://github.com/RakitaLabSoftware/rlsmorph/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/RakitaLabSoftware/rlsmorph/actions/workflows/build.yml)

## Installation
- **From pypi**
    ```bash
    pip install rlsmorph
    ``` 

- **Browse to your destination and download the repository locally:**
    ```bash
    git clone https://github.com/RakitaLabSoftware/rlsmorph rlsmorph
    cd rlsmorp
    ```
- **Create a virtual environment. For example**:
	-  python 
	
	```bash
	python -m venv .venv
	source .venv/bin/activate
	```
	- conda
	
	```bash
	conda create -n rlsmorph python=3.11
	conda activate rlsmorh
	```
> **Note**: If you are using an existing virtual environment - skip this step. But this is strongly recommended to work in some virtual environment

- **Install**: 
	- General installation:  `pip install -e .`
	- For developers also install: `pip install -e "[.dev]"`

## Structure
#### **Alignment main computational steps**:
1. Load source and target in a `np.ndarray`. 
     - Output: a numpy 2D matrix
2. `Preprocessing` #TODO
3. `FeaturePointDetector` finds the keypoints(coordinates and point size) and based on them exctracts descriptors(features) for each keypoint in image. 
     - Output: a list of (selection-reagion (point and area), features)
4. `Matcher` match the descriptors based on their similarity accoring to chosen algorithm.
     - Output: a sorted list of keypoints based on goodness of fit.
5. `Warper` is algorithm that compute the best transformation matrix(M) between provided target(t) and source(s) keypoints (s*M=t) and then apply it to source image. In other words it tries to decrease distance between the matched(sorted) keypoints between target and source given predetermined constraints for warping. For example a constain be that an image will only be rotated or freely distorted.
     -    Output: transformation matrix and warped source (transformed source image). Note that based on chosen algorithm of warper one may require different transformation(it could be 2d matrix or 3d matrix if we choose homography based algorithm).

#### **`from_config` method**:
The way we load the object type (for example: data, data type, functions (for matching, warping, etc.)), is via a config object (json, yml, pickle). Therefore we need a from_config method to setup the object that are going to be used in the workflow above.
#### **`Hooks`**:
"Hook" is an operation that can be acted on the outputs of each object. It is often defined after a core operation occurs, without interfering the flow, but allowing a side operation take place, such as visualization, caching etc.  Implementation-wise: an external function will always operate on a hook object.
## **Strategies for**:

### Preprocessing:
1. Apply convolution matrix to increase feature contrast. (elaborate) 
### Finding Feature Points
A Feature Point is described by the pair of Keypoint and corresponding Descriptor. Keypoint is basically coordinates (x,y),  and region around the selected coordinate (area of ROI). Descriptor is numeric representation of the image content(texture, gradient, change in contrast etc.) or in other way something that describes a property of ROI in an image.

To set keypoints we can use several approaches:
1. Manual Selection:
   - a user manually selects keypoints on both src and trg images by clicking on the images at locations she/he thinks are similar. This way we assure a possible ground truth, but also prone to human error.
2. Classical Computer Vision (CCV) Algorithm:
    - automatically detects keypoints based on descriptors that are present in the entire region of selection, where the keypoint selection is based on hand crafted(non machine learning) algorithm (ORB, SIFT, etc.) quantity of interest (QoI).
3. Machine Learning Computer Vision (MLCV) Algorithm:
   - Same as CCV, but the QoI is computed via a ML algorithm. Example will be ["Segment Everything"](https://segment-anything.com/) (SAM).

### Matching Keypoints
Matches refer to the correspondence between descriptors of different images. Matching is the process of finding pairs of descriptors that describe the same point or region in the scene. 

In SciMorph there is two matching algorithms:
1. NaiveMatcher:
     - Basically just returns list of `cv2.DMatch` without changing it order with fixed distance equals 0.5
2. FeatureMatcher:
     - Matches features points based on similarity of their descriptors.

### Warping 
After we found out how feature points of source image matches with feature points target we can make compute transformation matrix (which is basically just change-of-basis/transition matrix) and then apply this transformation to whole source image.
We could also set restriction for type of transformation matrix (dimentionality)
#### Transformation
1. Prespective
2. Affine
3. Rotation
4. Translation

## TODO:
- [x] Organize CCV - make a version with it
- [x] Explore MLCV - SAM, ect.
- [ ] Apply preprocessing post image load and prior to keypoint selection
- [ ] Output in warper both transformation_matrix, trasformation_method, transformed_source
