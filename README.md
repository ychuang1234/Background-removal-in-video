 <h1 align="left">Background removal in video</h1>
<h2 align="center">  
 
 ## Goal
 Construct mixture of gaussian model (GMM) to each pixel from each video frame and the **gaussain with larger prior distribution** are more likely to be the **static background**.
 
  ## Discription
  
 ### (1) Construct GMM model to simulate background scene
 Background modelling is the task of extracting the static background from a sequence of video frames. Once the background has been modelled, a technique called background subtraction which allows an image’s foreground to be extracted for further processing (object recognition etc.)
 
 ### (2) Generate the foreground mask through substracting input frame and background image
Background subtraction (BS) is a common and widely used technique for generating a foreground mask by using static cameras. BS calculates the foreground mask performing a subtraction between the current frame and a background model, containing the static part of the scene.

 
 ## Result

 ### (1) Foreground mask of one video frame 
 <p align="center">
<img src="https://github.com/ychuang1234/Background-removal-in-video/blob/bc25edb685690ccf6d60c3991704dd1fbe9b47a7/result_fgmk.JPG" width="80%">
 </p>
  

 ### (2) Video frame with rectangles which indicate the forground (or not considered as background in estabilished GMM)
 
  <p align="center">
<img src="https://github.com/ychuang1234/Background-removal-in-video/blob/bc25edb685690ccf6d60c3991704dd1fbe9b47a7/result_rect.gif" width="80%">
 </p>
 
