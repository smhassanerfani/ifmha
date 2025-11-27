# IFMHA: Inventory of Field Measurement for Hydraulic Attributes

<a href="https://opensource.org/licenses/MIT" target="_blank">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
</a>

## Dataset Access

### Working with Git LFS

This repository stores IFMHA dataset with Git LFS, use the steps below to install and fetch them.

- **Install (macOS / Homebrew):**

    ```bash
    brew install git-lfs
    git lfs install
    git lfs version
    ```
- **Install (Ubuntu / Apt):**
  
    ```bash
    sudo apt update
    sudo apt install git-lfs
    git lfs install
    git lfs version
    ```

- **Clone + download LFS objects (automatic):**

    ```bash
    git clone https://github.com/smhassanerfani/ifmha.git
    cd dataset
    git lfs pull
    ```


Note: For private repositories use SSH or a Personal Access Token (PAT), and monitor GitHub LFS storage and bandwidth quotas.

### Alternative Download (Google Drive)

If IFMHA repository reaches the 10 GB bandwidth limit, download the dataset directly from Google Drive: https://drive.google.com/file/d/1X3la64OP8Hpa6dAsqxMmRp0Ym2xJrJ5B/view?usp=sharing


## Dataset Description

IFMHA includes 2,802,532 field measurements collected at 10,050 USGS gage sites across the US. 
The time span of these measurements is from `05-05-1845` to `10-24-2022`. IFMHA extends the HYDRoSWOT dataset with
the entire record of field measurements within NWIS including different types of field measurement methods 
(see Table 1). The number of unique gage sites included in IFMHA is 10,050 which is 31 sites less than HYDRoSWOT
(17 of these stations are operated by an agency other than USGS, and the data for the other 14 stations are not 
available on the USGS website). IFMHA augmented the NWIS field measurements by adding relevant attributes reported 
in the NHDPlusV21 dataset.

Table 1. The different types of USGS streamflow field measurements methods.

| Method | Description                                | Frequency | Percent |
|--------|--------------------------------------------|-----------|---------|
| UNSPE  | Unspecified                                | 1204516   | 43.19%  |
| QSCMM  | Discharge, measured, midsection method     | 792169    | 28.40%  |
| QADCP  | Discharge, measured, ADCP from moving boat | 437418    | 15.68%  |
| OTHER  |                                            | 347104    | 12.45%  |
| QFLUM  | Discharge, measured, flume                 | 3888      | 0.14%   |
| QIDIR  | Discharge, measured, indirect method       | 2959      | 0.11%   |
| QVOLM  | Discharge, measured, volumetric            | 900       | 0.03%   |
| NONE   |                                            | 4         | 0.00%   |
| ACOUS  | Acoustic Doppler Current Profile (ADCP)    | 2         | 0.00%   |
| ESTIM  | Estimated                                  | 1         | 0.00%   |


IFMHA consists of three main sources of data including HYDRoSWOT, NWIS field measurements, and NHDPlus V2 datasets.
The order and process of incorporating each dataset for the compilation of IFMHA are depicted in Figure 1.
The flowchart outlines the sequential steps involved in dataset adoption.


<p align="center">
    <img src="https://github.com/smhassanerfani/ifmha/blob/main/figures/fig01.png?raw=ture"
    alt="Main Sources of Data" width="100%" height="100%">
    Figure 1. Flowchart illustrates the incorporation of data sources for the compilation of IFMHA.
</p>

## Dataset Field Attributes

### NWIS Field Measurements
For the compilation of IFMHA, field measurements were queried in a tab-separated format from 
[NWIS Site Inventory](https://waterdata.usgs.gov/nwis/inventory) and then parsed and converted into a unified 
data frame comprised of records for all sites. For this purpose, URL links for each USGS site station were first 
created using the list of site numbers in the HYDRoSWOT dataset. Then, field measurements for each site station were 
queried from the NWIS Web Interface using the URL links. Finally, the requested text file of each site was 
parsed into a unified data frame. 

### HYDRoSWOT
HYDRoSWOT is an extensive collection of USGS cross-section surveys for supporting Surface Water Oceanographic Topography
(SWOT). The dataset comprises over 200,000 records of USGS Acoustic Doppler Current Profiler discharge measurements 
collected from the USGS streamgaging network. It offers a range of essential fields, including mean and maximum depth, 
velocity, discharge, stage, and water-surface width.
IFMHA borrows `station_nm`, `dec_lat_va`, `dec_long_va`, `site_tp_cd`, `drain_area_va`, `contrib_drain_area_va` 
features from [HYDRoSWOT](https://data.usgs.gov/datacatalog/data/USGS:57435ae5e4b07e28b660af55).

### NHDPlusV2
National Hydrography Dataset Plus (NHDPlus) is a national geospatial surface water framework including the features 
and capabilities of the National Hydrography Dataset (NHD), the National Elevation Dataset (NED), and the Watershed 
Boundary Dataset (WBD). NHDPlus integrates the vector NHD stream network and WBD hydrologic unit boundaries with the 
NED gridded land surface.
IFMHA includes `COMID`, `STATE_CD`, `STATE`, `DASqMi`, `DASqKm`, `LatSite`, `LonSite` as well as `FTYPE`,
`StreamOrde`, `SLOPE` which are borrowed from NHDPlus_GageLoc and NHDPlus_NHDFlowline_Network of 
[NHDPlusV2](https://www.epa.gov/waterdata/get-nhdplus-national-hydrography-dataset-plus-data). 


## Reference
Please cite the following papers when referencing this work or any of the foundational concepts discussed, and use the provided links to find the manuscripts:


  * **[Manuscript at Environmental Modelling & Software](https://www.sciencedirect.com/science/article/abs/pii/S136481522400197X)**

    ```bibtex
    @article{erfani2024large,
    title={A large dataset of fluvial hydraulic and geometry attributes derived from USGS field measurement records},
    author={Erfani, Seyed Mohammad Hassan and Erfani, Mahdi and Cohen, Sagy and Downey, Austin RJ and Goharian, Erfan},
    journal={Environmental Modelling \& Software},
    volume={180},
    pages={106136},
    year={2024},
    publisher={Elsevier}
    }
    ```