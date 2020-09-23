This *FPNet demo* is able to reconstruct walls in areas with overlapping graphics or nonuniform patterns, thus allowing the room structures to be recovered even from complicated drawings.  


<figure>
  <img src="./imgs/Fig. 1.tif" alt="Caption text">
  <figcaption>Fig. (a) input floor plan images and our results of (b) the style-transferred plans and (c) the vectorized floor plans</figcaption>
</figure>

**Deep Floor Plan Analysis for Complicated Drawings Based on Style Transfer**  
[[Seongyong Kim](http://syoi92.github.io)], [[Seoula Park](https://)], [[Hyengjung Kim](https://)], [[Kiyun Yu](https://)]  
Journal of Computing in Civil Engineering, 2020.
***
#### How to run this demo
The demo requires Python =< 3.6 (The version of TensorFlow we specify in*requirements.txt* is not supported in Python 3.7+).  

```
git clone https://github.com/streamlit/demo-face-gan.git
cd demo-fpnet
pip install -r requirements.txt
streamlit run app.py
```


#### Citation
```
@article{FPNet2020, 
title={Deep Floor Plan Analysis for Complicated Drawings Based on StyleTransfer}, 
author={Seongyong Kim, Seula Park, Hyeongjung Kim, Kiyun Yu}, 
journal={Journal of Computing in Civil Engineering}, 
year={2020}, 
DOI={10.1061/(ASCE)CP.1943-5487.0000942}}
```

#### Acknowledgments
Code borrows heavily from [[Isola *et al*](https://github.com/phillipi/pix2pix)]. The floor plan datasets originated from *EAIS-fp* [[Jang *et al*](https://)] and *SNU-fp* [[Kim *et al*](https://)], and in purpose of increasing the varsarity of the datasets, we added more drawings in diverse formats.