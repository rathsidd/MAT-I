# Applications for MatI
## Python Image Analysis modules
### Contents
* **background correction** `from pia import back_corr as bc`
	* in *scikit-image*
	* in *openCV*
	* renormalization
* **Segmentation** `from pia import segmentation as sg`
	* in *scikit-image*
		* gabor segmentation `sg.gabor`
		* random walk segmentation `sg.rw`
		* edge based segmentation `sg.eb`
		* region based segmentation `sg.rb`
		* watershed segmentation `sg.wrs`
	* in *openCV*
		* watershed segmentation
		* gabor
		* other
		* other
* **subsampling**
	* size of image
	* subsample
* **binarization**
	* Binarization of regions
* **Edge detection**
	*Canny
	* sobel
	* prewitt
	* roberts
* **Parameterization**
	* volume fraction
	* percent coverage of ordered phase
	* percent coverage of peptide
	* roughness distribution
	* height distribution
	* orientation distribution
	* aspect ratio distribution
	* order:disorder ratio distribution
	* FFT
* **Clustering**
	* k-means
	* k-nearest neighbors
* **Prediction**
	* Average pH, distributions
	* Average Concentration, distributions
	* Average incubation time
	* Applied voltage pattern
	* probable sequence
	* probable substrate
	* Buffer composition used
	* Average Temperature 
* **Convolutional Neural network**
	* *wavelet decomposition*
		* PDB
		* Sequence
		* Substrate
		* Other Params
		* images
		* signals
		* other results
	* Fingerprinting
		* hashing
		* fingerprinting
			* dendritic
			* wave
			* other
	* *building a CNN*
	* *Training a CNN*
	* *clustering*
	* *predictions*
# MAT-I
