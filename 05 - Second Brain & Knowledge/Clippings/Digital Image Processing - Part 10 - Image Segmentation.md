---
title: "Digital Image Processing - Part 10 - Image Segmentation"
source: "https://www.youtube.com/watch?v=O2rocj9mJvM&list=PL2mBI0yFsKk-p73KQ4iPdsi10hQC4Zd-0&index=10"
author:
  - "[[ASIP-Lab]]"
published: 2020-08-10
created: 2026-08-12
description: "Topics:00:22 Fundamentals of Image Segmentation15:32 Point Detection19:53 Line Detection23:54 Edge Detection52:48 Image Thresholding"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=O2rocj9mJvM)

Topics:  
00:22 Fundamentals of Image Segmentation  
15:32 Point Detection  
19:53 Line Detection  
23:54 Edge Detection  
52:48 Image Thresholding

## Transcript

**0:00** · Hello everyone, welcome to the 10th lecture of the digital image processing course on image segmentation.

**0:08** · In today's lecture, I will go over some fundamentals of image segmentation, introduce some techniques for point detection, line detection, and edge detection, and finally some techniques for image thresholding.

### Fundamentals of Image Segmentation

**0:23** · So, let us give you some properties and definitions for image segmentation.

**0:29** · Let's just assume we have image I.

**0:34** · And I here represent the entire spatial domain or region of the image. So, image segmentation is the process of dividing this image I into several partitions. So, these partitions are going to be numbered as R1, R2, all the way to Rn.

**0:52** · So, these partitions partitions satisfy some properties.

**0:57** · The first property is in terms of the union. So, the union of uh all these regions or partitions Ri for I changing from 1 to n equals the entire image.

**1:12** · The next property is with respect to the connectivity. So, each one of these individual regions is considered to be a connected set.

**1:22** · And this is something that you can refer to one of the earlier lectures of the course when we were talking about connected sets.

**1:31** · The other property is with respect to their intersection. So, the intersection of Ri and Rj for any I and J that are not equal is going to be the null set. So, there is no uh intersection between these regions.

**1:48** · And finally, we have the intra-region similarity and inter-region dissimilarity properties for these uh partitions. For the inter-region similarity, uh if we have Q as a logical predicate or condition defined to do the partitioning or segmentation in the first place, this Q is going to be true for each one of these individual uh partitions.

**2:21** · And it is going to be false for the union of these each one of a pair of these uh partition. So, to put it in simpler terms, whatever property that we used to do the segmentation should be true within each of these segments, and should be not true for the union of two uh two segments or two partitions.

**2:49** · So, let's say you are you're using the intensity values to do the segmentation, right?

**2:58** · So, all the pixels that are in the same region, they need to have similar uh intensity values because the similarity because the intensity values was the measure for doing the segmentation. On the other hand, two regions that are different, uh if you you calculate the their union, um the logical the condition Q should be false.

**3:28** · If it's true, that mean that both of them are basically the same segmentation. So, whether the image segmentation is wrong or uh if it's true, then the Q for the union of Ri and Rj should be false.

**3:47** · So, segmentation algorithms are generally based on two basic categories.

**3:52** · We have discontinuity-based segmentation in which uh boundaries of regions are sufficiently different from each other and from the background.

**4:04** · And edge-based segmentation is one example of continuity discontinuity-based segmentation.

**4:11** · And then we have similarity-based segmentation in which uh you partition an image into regions that are similar according to uh some criteria. For example, region-based segmentation is an example of a similarity uh based segmentation.

**4:29** · So, let's just take a look at one example here on top left, we have uh an image uh of a blob. The inside of the blob has a constant intensity, and the outside, which we called it here background, had also a constant intensity.

**4:49** · So, if you want to do the segmentation based on the discontinuity, what we need to do is that we need to detect the boundary between these two regions. So, in the middle, we have the boundary based on the intensity discontinuity discontinuities of these two regions.

**5:06** · And then finally, we have the result of segmentation that has the the blob as white or one class, and has the background uh black or the other class.

**5:21** · So, let's just take a look at another example. Here, we have uh an image of a blob, but this time uh the intensity inside the blob is not uh constant, but it has a texture. And as you can see, the the texture is pretty uniform across the blob.

**5:43** · And the difference between the blob and its background is basically from its texture.

**5:50** · So, now to do the segmentation, one idea is to calculate the um the edges in the whole image, and then do the segmentation uh based on the calculation of the edges uh that we see in the image.

**6:07** · So, if we apply the either the gradient or the Laplacian to detect the the edges uh or uh discontinuities in the intensity, what we end up with is in the background, since there was no difference in the intensities, we have all black values, but inside the object, we have values that are not black. So, you have both white and black pixels.

**6:39** · So, now this can be used as a measure to distinguish uh the background from the object. And finally, you see the result of segmentation based on uh the region properties.

**6:54** · So, as you can see, we need to find ways to detect boundaries or the edges in the images to be able to um distinguish between different objects.

**7:09** · So, this is not necessarily all that we need, but it is a basic uh foundation that we can use. So, because of that, let's just review what we learned before uh for calculating the derivatives inside the images.

**7:27** · So, we saw that by doing local averaging, we can smooth an image. On the other hand, we saw that intensity variations can be detected by first or second-order derivatives. So, generally speaking, derivatives in images are done in terms of finite differences because in images, we have uh a discrete domain.

**7:50** · So, the derivative can be estimated in the discrete domain by finite differences.

**8:01** · So, if you remember from before, we had some properties for the first and second-order derivatives that need to be satisfied.

**8:09** · So, for the first-order derivative, it should be zero in the areas of constant intensity.

**8:16** · Uh it should be non-zero at the onset of an intensity step or ramp. And finally, it should be non-zero along intensity ramps.

**8:25** · On the other hand, second-order derivative must be zero in areas of constant intensity, must be non-zero at the onset and end of an intensity step or ramp.

**8:37** · And finally, it must be zero along intensity ramp.

**8:42** · So, we have seen these properties before.

**8:45** · So, we had several uh equations or estimations for the first and second-order derivatives. So, for the first-order derivative, we can have a forward difference formulation in which the first-order derivative of any pixel is basically the difference uh between the function value at the next pixel minus the function value at the current pixel.

**9:16** · We can have a backward difference estimation.

**9:20** · And finally, we can have a central difference estimation.

**9:23** · As you can see, for the central uh difference estimation, we have this denominator of two, and that's why uh and that is because we are calculating the values the difference between the values of two pixels that are are two pixels apart. So, they are in uh either side of the the central pixel.

**9:49** · And that's why it's called the central difference.

**9:52** · If we extend these definitions to get the estimation for the second order derivative, the common way is to have a second order central difference in which as you can see the second derivative of function f and location x is going to be f of x + 1 - 2 f of x + f of x - 1.

**10:15** · So you can extend these equations to find the central derivative for higher uh derivative as well. So here in this table we have the central difference for the uh first order derivative in the first line, then for the second order derivative and then the third and the fourth order uh derivative.

**10:40** · Just pay attention that for the first and for the third order derivatives we have these constant uh tools that are multiplied.

**10:52** · And the reason for that is to calculate this, we are actually using the uh pixels or the points after and before the actual pixel that we want to find the derivative for. And that's why we have this uh constant of two multiplied by the uh first and third order derivatives.

**11:19** · So this is something that we have seen before as well.

**11:26** · First derivative when applied to images usually produce thick edges in images.

**11:33** · On the other hand, second order derivatives have a stronger response to find details such as thin lines, isolated point, and noise.

**11:43** · Also, there was another property for second order derivative.

**11:48** · Uh And that property was that second order derivative produce double edge response at ramp and step transitions. And that was useful to locate edges.

**12:01** · And finally, the sign of the second order derivative can be used to see if there was a transition into an edge uh going from dark to light or light to dark uh in the image. So we can see all these properties here uh as well. So here, let us say we have this sample image. And what we want to do is that we want to find the first and second order derivatives for uh a a linear profile inside this image.

**12:31** · So this is the line that we want to calculate the first and second order derivative uh along it. So if we uh plot this uh line of intensity values as a one-dimensional function, this is the function that we have.

**12:53** · We have a uh ramp-like transition in the intensity because of this region we have this very bright uh dot at this location, then we have this uh line uh in which we have a shape uh like a roof shape uh

**13:17** · edge, and finally we have this uh sudden transition or a step transition that we have at the end because of going from dark to light in this region of the line.

**13:31** · So we can use any of the equations that was provided in the previous slide to calculate uh the first and second order derivatives.

**13:42** · So here you can see uh we have put intensity values uh instead of drawing it as a function. In the next row we have the values for the first order derivative and we finally we have the value for the second order derivative. As you can see for the intensity ramp, the value for the first order derivative is non-zero.

**14:07** · Then for the regions of uh constant intensities, we have the values for the first order derivative to be zero at locations of uh rapid changes in the intensity, we have non-zero values.

**14:29** · Uh As for the second order derivative, the only difference was second order derivative should produce zero values for uh intensity ramps. And that is basically what you see here, too.

**14:46** · That uh in this region which is associated with the second order derivative of this intensity ramp, what we have is the second order derivative is uh is zero.

**15:01** · So if you take a closer look look at all these values and pay attention here that we have ramp intensity changes, we have isolated points, we have uh uh line segments or roof shape edges, and finally we have a step edges.

**15:23** · You see that all the properties that are mentioned here are valid for the first and second order derivatives.

### Point Detection

**15:34** · So now let us see what how we can use second order derivative for detecting isolated points in the image.

**15:44** · So if you remember from before we have seen the equation for the Laplacian and it was defined as the summation of the second order derivative with respect to the horizontal and vertical axis in the image.

**15:58** · If we use a central difference formulation the the equation for the Laplacian can be summarized as this equation. We can uh use a 3 by 3 kernel to represent this equation as well. So to to get the Laplacian of an image, what we need to do is to find a convolution between this 3 by 3 kernel and the uh and the image.

**16:34** · And the result at any given point will be the Laplacian value uh of the of the image at that point. So now let's see how we can use this to uh detect isolated points in the image.

**16:51** · So there are three steps that we need to follow. First, we need to compute the Laplacian response of the image at every pixel. And as I said, this can be done by uh calculating the convolution between the 3 by 3 kernel and the image.

**17:09** · Then we can take the absolute value of the Laplacian response.

**17:14** · If you remember uh the Laplacian can be either positive or negative. So since we uh want to detect the locations of the isolated point and we don't care about whether the value of Laplacian is positive or negative what we do is basically we take the absolute value. So now all the values are going to be positive.

**17:37** · And then finally we provide a threshold.

**17:40** · Uh And if the result of the previous step is greater than threshold for any given pixel, we set the pixel to one.

**17:50** · Otherwise, we set the pixel uh to zero.

**17:53** · So this can be shown mathematically using this equation. So g of x and y, which is the result of this point detection, is going to be one if the absolute value of the Laplacian at that location is greater than the threshold and it's zero otherwise. So any location in g of x and y uh which has a value of one is an isolated point and the locations that are zero are not isolated points.

**18:26** · So you can see an example here, too. So here we used a a different kernel for Laplacian. So the previous kernel, if you look closely, only calculates the Laplacian along the horizontal and vertical axis.

**18:40** · This one is isotropic with respect to uh horizontal, vertical, and and the diagonal axis as well.

**18:51** · Uh The second image is an x-ray image of a turbine blade uh in which we have a defect in um in this region. So what we can do is that we can calculate the Laplacian of the image. So when you calculate the Laplacian, you basically eliminate all the regions of constant intensity.

**19:17** · And as you can see here, we have a little bit brighter dot at the location of the defect in the uh in the image. So now what is left to do is that you provide a a proper threshold. And by doing that, you can isolate this uh uh this point further. And that is the result of applying a properly defined threshold.

**19:42** · So the on the location of the defect is being shown with this uh arrow here.

### Line Detection

**19:54** · We can use the first and second order derivatives to detect lines in the images, too.

**19:59** · So, here we use second order derivative to detect lines in the images.

**20:05** · And the reason for that is uh second order derivative uh result in a stronger filter response uh and also thinner lines in comparison to first order derivative. So, let's just take a look at one example.

**20:18** · So, on top left, we have this original image in which we want to detect uh lines uh in the image. So, what we do is that we calculate the Laplacian of the image.

**20:33** · And this is by applying any of the kernels that we we used before for calculating the Laplacian. So, as you can see here, we have a magnified view of this small region here, and as you can see, as mentioned before, in the when we calculate the Laplacian, uh at locations of uh lines and edges, what we have is that we have a region of positive value and a region of uh negative value.

**21:02** · So, in effect, we have uh a double line showing uh the the location of the the edges.

**21:12** · So, now let's see. We want to uh only work on work based on the absolute value. So, this is the result of finding the absolute value of the Laplacian. As you can see, the edges are uh very thick.

**21:33** · What we can do is that we can only use the positive values.

**21:38** · So, that means that we apply a threshold of zero, and when we do that, this is what we end up with uh as for the location of the lines in the image, which are shown with very thin uh lines.

**21:55** · What if we want to locate lines that are not only in horizontal and vertical direction? So, in this case, we can use modified kernels to to achieve this.

**22:08** · So, here is the set of four kernels that we can usually use.

**22:14** · This one is for detecting horizontal line. This one is for detecting line uh with the angle 45°.

**22:22** · This one is for vertical line, and this one is for detecting angles in the direction -45°.

**22:30** · So, here we have the same image as before, and the goal here is to detect uh diagonal lines uh in the direction of uh positive 45°.

**22:42** · So, what we do is that we uh apply this kernel into the image by doing 2D convolution, and this is the result of applying the the convolution. Here, you see a zoomed view of the result for the top left corner, and here you see the zoom view for the bottom right corner kernel uh corner of the uh the image.

**23:13** · Now, what we can do is that we can apply uh a threshold to to this image, and if we do that, this is the result that uh that we get.

**23:30** · Uh if we change the value for the threshold and put put it at 254, what we end up with is this image in which only the the edges uh in these directions very close to 45° uh to degree directions are uh are highlighted.

### Edge Detection

**23:54** · So, let's just take this to the next level and talk in more general terms.

**24:00** · So, here I want to talk about edge detection.

**24:03** · So, edge detection is a common approach for image segmentation based on local intensity changes and discontinuities.

**24:10** · So, there are three different types of edges in the images.

**24:15** · We can have step edges in which a transition between two intensity levels usually occur ideally uh over the distance of one pixel. So, this is an example of a step edge, ideal step edge. Then, we can have the ramp edges in which we have a gradual transition between two intensity levels.

**24:36** · So, this is an example of an ideal ramp edge. As you can see, we have this small transition from one intensity level to another one.

**24:47** · And then finally, we can have roof edges in which intensities on both sides of the roof are similar, like we have here, but we have different intensity in the middle of the image.

**24:59** · So, this is an ideal example of a roof edge.

**25:04** · So, let us see uh what we can expect in real images. So, here we have a real uh CT image of a brain.

**25:17** · If you look closely in this region, we have uh a rough estimate of a ramp edge. We have a smooth transition from two between two intensity values.

**25:31** · Here, we have an example of a roof edge.

**25:34** · And finally, we have an approximate a step edge.

**25:39** · So, as you can see, uh in practical application, you don't exactly see what you see in the uh ideal cases, but it is still close enough.

**25:54** · So, the first derivative, as we said before, produces thick edges uh in the images. On the other hand, second derivative produces a double edge profile with a sign change.

**26:08** · And the point at which uh we cross zero can be used to locate the edges. So, let's just uh take a look at one example here. So, here what we have is an example of a uh ramp edge. As you can see here, we have a smooth transition from this intensity value to this intensity value.

**26:30** · If we calculate the the first order derivative, what we get is the first order derivative is going to be non-zero uh within the ramp, and it's going to be zero outside. On the other hand, for the second order derivative, we have two spikes in which uh one is positive and the other one is negative, and that's what uh I mean by a double edge profile.

**26:59** · So, how can we locate the um the edge by taking the average of the location of these two uh spikes, or basically, wherever this uh this line that takes the average crosses zero. So, that is a way to locate the edge.

**27:19** · Of course, depending on different application, uh we can use either first derivative or second order derivative, but usually, second order derivative is more preferred.

**27:35** · So, now, let's just see what happens if we have uh a noisy image.

**27:42** · So, here you have the ideal cases uh as we saw in the previous uh slide, we have this ideal uh ramp edge. We have the the first order derivative, and we have the second order derivative. So, these uh samples are without any noise. So, now, let's just see if we add some Gaussian noise with a zero mean, but standard deviation of 0.1 uh intensity values.

**28:17** · So, this is still the This is basically the noisy image. Of course, since the level of noise is uh not very large, it is very hard to see it here. But, on the other hand, in first and second order derivative result, we have more sensitivity to noise because uh since we are calculating the the difference between neighbor pixels, um this magnifies the amount of noise.

**28:52** · As you see here, this is the result of calculating the first order derivative for this uh noisy ramp edge, and the amount of noise in the first order derivative is definitely more visible than the original image. As for the second order derivative, it is more sensitive to noise. As you can see, the two originals uh spikes are hardly visible here.

**29:21** · If you increase the amount of noise for the second order derivative, you don't you cannot even detect these spikes anymore.

**29:33** · The same happens for the first order derivative. Of course, it it happens uh less than the second order derivative. Uh and that's why if you are with noisy images, um usually first-order derivative is preferred than second-order derivative.

**29:53** · Of course, you can always eliminate the effect of noise by using um smoothing filters before detecting edges.

**30:05** · So, let's just go over the first-order derivative again and talk about the concept of image gradient.

**30:13** · So, the gradient of an image f of x and y is defined as a two-dimensional column vector for any individual pixel.

**30:23** · And the components of this two-dimensional vector for each point is going to be the the derivative along the horizontal axis and the derivative along the vertical axis.

**30:39** · These are the thing that I've discussed them before as well.

**30:43** · So, the magnitude of the gradient vector at any location is calculated by this equation.

**30:51** · And the direction of the gradient vector is calculated by this equation. So, now the question becomes how can we calculate the gradient with respect to the horizontal and vertical direction?

**31:06** · And the answer to that is very simple.

**31:08** · We use a set of uh predefined kernels.

**31:14** · And these kernels are derived based on the the finite difference estimate that we have.

**31:21** · So, we have the set of Roberts kernel, which are uh 2x2 kernels that are used for detecting diagonal edges.

**31:31** · We can have uh Prewitt kernels, which are 3x3 kernels.

**31:37** · And then we can have Sobel kernels. And uh these are not the only kernels that you can use for calculating the gradient uh or the first-order derivative along the horizontal and vertical uh axis, but these are the very common ones.

**31:57** · So, let's uh take a look at one example here. Here, as you can see, we have this image in which we have a transition between intensity values going from dark intensity to bright intensity. And as you can see, the edge is along the diagonal axis.

**32:16** · What we can do with image gradient is basically to uh not only get the magnitude of the edge, but also we can calculate the edge direction based on the the gradient that direction of the gradient vector. And that can that is visible uh in this example, too.

**32:38** · So, as you can see, the edge direction is along the uh diagonal axis.

**32:45** · And the gradient vector is basically perpendicular to the to the edge direction.

**32:52** · So, this is as opposed to using second-order derivative because with second-order derivatives, we don't get any information on the edge direction. What we only get is basically the strength of the Laplacian at any location in the image.

**33:11** · So, if the goal is only to detect the location of edges, maybe third second-order derivative is more preferred. But if you want to have more information, especially on the direction of the edges, usually first-order derivative and of course, image gradient are more preferred.

**33:33** · So, let's just take a look at more examples. On top left here, we have an original image.

**33:41** · Uh this one is the absolute value of the gradient in the x direction. And this one is the absolute value of the gradient in the y direction. And these are calculated by using uh horizontal and vertical Sobel kernels.

**33:59** · And finally, this is the magnitude of the gradient image that is approximated by sum of the absolute values of uh gradient in the x direction and in the y direction.

**34:12** · What happens if we apply a smoothing before we calculate uh the gradient?

**34:20** · If we apply a smoothing, we practically eliminate some of the minor intensity changes.

**34:30** · So, what we end up with is a better representation of the uh stronger intensity intensity changes in the image. So, these images are basically the same result as before, but now we have a smoothed the original image by a uh 5x5 averaging kernel.

**34:52** · And as you can see, a lot of the very fine uh gradient values that we had in these regions are completely eliminated when we apply a smoothing before we calculating the gradient.

**35:08** · So, the previous kernels are only able to differentiate between horizontal and vertical edges.

**35:14** · We can uh extend those kernels to uh to detect directional uh edges as well.

**35:22** · So, for the Prewitt kernels, we can use these two kernels to detect directional edges or calculate directional uh changes of intensity.

**35:36** · And we can use these two kernels uh for the for the Sobel uh approach to calculate directional edges as well.

**35:46** · But again, these are not the uh only ones that you can use.

**35:52** · There is a very famous set of kernels that are designed to detect edge magnitude and direction in all eight compass directions. It's called Kirsch compass kernels.

**36:04** · So, these eight kernels are basically the set of uh Kirsch compass kernels.

**36:10** · So, instead of using the equations that we defined before to calculate the and direction of the edges, uh in this approach, we determine the edge magnitude by convolving of the image with all of these eight kernels. And then we assign the edge magnitude at any given point as the response of the kernel that gave the strongest convolution value at that point.

**36:37** · And for the edge direction at any given point, we use the direction associated with the kernel with the strongest uh convolution response at uh any given point. As you can see, when using Kirsch compass kernels, um the the set of directions that uh you end up with are prefixed uh as opposed to what we had before.

**37:04** · So, if you use a Sobel kernel, what we you can have is a a a bigger set of values for the direction of edges.

**37:18** · For the Kirsch compass kernels, what you have is only a kernels along these uh directions along these uh eight uh compass directions: north, northwest, west, southwest, south, southeast, and east, and northeast.

**37:38** · So, now that we have seen this, let us talk about uh a more advanced technique for detecting edges. And that is Canny edge detector. So, the Canny edge detector uh is built based on three main objectives. So, we want to have a low error rate. So, we don't want to uh locate edges that are wrong. So, basically, we want the location of the edge to be as accurate as possible.

**38:11** · The second objective is that edge points should be well localized. So, as you can see, it has some overlap with the with the first uh objective as well.

**38:23** · And then finally, we want to have single edge point response. If you remember from before, we said that when we use um Laplacian to detect edges, we end up with two locations for any edge.

**38:37** · Uh And for the uh first-order derivative, if we use that for uh detecting edges, we ended up with uh thick edges. So, one of the main objectives of Canny edge detector is that we want to have edges with only uh one single pixel at width.

**39:02** · So, based on these uh requirements, Canny edge detector involves four main steps.

**39:10** · First, we have to uh smooth the input image using a Gaussian filter.

**39:14** · Uh so, this way, what we uh do is basically eliminate a lot of the uh smaller changes of intensity in the image.

**39:26** · And that helps us reduce the error rate and uh unnecessary or weak edge points.

**39:37** · Then we compute the gradient magnitude and direction of the image.

**39:42** · On the third list of the apply non-maximal suppression to the gradient magnitude and finally we use double thresholding approach and also connectivity analysis to detect and link edges.

**39:58** · So in a step three we use non-maximal suppression of the uh gradient magnitude and that is for thinning the gradient magnitude near the edges.

**40:09** · So to do that we assume G subscript N of X and Y as the result of thin thinning of the gradient image.

**40:20** · And this is how we perform non-maximal suppression.

**40:26** · Uh so in the first step we find the direction closest to the gradient at location X and Y. So this basically is done for all the locations in the image.

**40:37** · So for any location we find the um direction of the gradient at that location and depending on the location we end up with two uh neighboring pixels. So let's just say we are working with pixel P5 and we find the gradient direction to be uh in this direction diagonal. So in this case P3 and P7 are going to be the two neighbors of P5.

**41:04** · Now what we can do is that if the magnitude of the gradient at location X and Y is less than the gradient of one of the two neighbors in that direction we set the value for GN at location X and Y to zero. So basically we suppress that. Otherwise we keep it there. So let's just see how it looks.

**41:31** · So we said that the the general direction let's just say it's in this direction. So we compare the magnitude of P5 with magnitude of P3 and magnitude of P 7.

**41:46** · So if the magnitude is uh greater than magnitude of P3 and P7 we keep it there. But if it's a smaller than the magnitude of any of these two pixels we suppress that.

**41:59** · And we do this for all the individual pixels.

**42:04** · And what we get is basically a thin gradient image. So this is to reduce the uh the amount of uh pixels with low gradient. But this is a still not enough.

**42:21** · In a step four we apply double thresholding and then we do connectivity analysis to uh remove uh weak edges even further.

**42:35** · So to do this we define two threshold values TH and TL and then based on these we generate two binary images.

**42:44** · One GN of H is basically GN greater than greater than or equal to TH. So basically any uh pixel from the previous step that has a gradient value greater than TH is going to be assigned a value of one in GN of H.

**43:07** · And for GN of L any uh pixel with a gradient value greater than or equal to TL will be assigned a value of one in GN of L. As you can see since TH is greater than TL all the uh all the values all the pixels with value one in GN of H will also be included in GN of L.

**43:33** · So since we want to have a separation between a strong edges and uh weak edges what we do next is basically we update GN of L and we subtract all the values that are uh basically common between the two.

**43:51** · So we calculate the subtraction between GN of L and GN of H.

**43:58** · So now to do connectivity analysis we uh follow this four-step procedure. We locate the next unvisited edge pixel P in GN of H X and Y.

**44:13** · We mark it as valid edge pixel.

**44:16** · All the weak weak pixels in uh GN of L that are connected to P using uh eight-point connectivity.

**44:26** · If all non-zero pixels in GN of H have been visited go to a step D. Otherwise you return to a step A.

**44:35** · And finally set to zero all pixels in GN of L that were not marked as edge pixel.

**44:42** · So basically what we do is that we go through all the pixels in GN of H for which the value of GN of H is one and then uh we look for neighboring pixels uh in GN of L to that uh pixel in the location X and Y and if there are any weak pixels there we mark them as valid. Otherwise we eliminate them.

**45:10** · And you will repeat that for all the uh edge pixels in GN of H.

**45:19** · So now let's just see what is the end result of all these procedures.

**45:25** · So on the left we have two input images uh that we want to use to to compare the result of regular edge detection and Canny edge detection.

**45:40** · In the middle we have the result of uh using image gradient magnitude for detecting edges and as you can see depending on the strength of the edge or the the shape of that uh we have edges that are uh different in thickness. So for example here we have very thick edges. Here the edges are even thicker.

**46:06** · There are regions that we don't have edges.

**46:10** · Uh the same is true for this one as well.

**46:14** · Uh but if we do Canny edge detector and if we follow all the procedures these are the result that we get. As you can see we have a much better representation of the edges.

**46:25** · Of course all the information about the direction and the strength of the edges are lost in the result of Canny edge detector. So depending on the application it's recommended to either use this one using the gradient in which you have both the information for the gradient magnitude and gradient direction or if you only want to know the location of the edges very accurately you can use Canny uh edge detector.

**46:56** · Of course you don't have any information on the magnitude or the direction of the edges if you uh use Canny edge detector.

**47:07** · So we briefly said that with Canny edge detector we do edge linking as well. So I'm not going to go uh too deep about edge linking. I just briefly mention what edge linking is and why it is useful.

**47:23** · So usually the result of edge detected detection is affected by noise or breaks in the edges that are caused by non-uniform elimination and some other effects.

**47:36** · That's why edge detection is commonly followed by edge linking.

**47:40** · So there are two different classes of edge linking.

**47:43** · Uh in local edge linking the gap between two edge points is filled if they have similar gradient magnitude and direction.

**47:53** · So let's just take a look at one example. Here what we have on the top left we have the image of the uh back of a vehicle.

**48:02** · In the middle we have the gradient magnitude and to the right we have uh horizontally connected edge pixels. So all the pixels that belong to edges and are uh all the edges are horizontal they are now connected together.

**48:21** · Here we have all the pixels edges uh that are vertical connected together.

**48:30** · Finally we have the the logical or of these two results and then we can use some morphological techniques uh for for thinning the edges. Of course we didn't get to talk about morphology uh in this course but the procedure is similar to uh edge suppression that we saw when we were working with um Canny edge detector.

**48:58** · But the whole point for local edge linking is uh if there are pixels in each other's neighborhood which have the a similar gradient magnitude and direction then we connect them uh together. Otherwise we don't uh we don't connect them. So as you can see here we need to know some information about the the edges uh beforehand.

**49:23** · So for example here we knew that we wanted to connect all the horizontal edges together or we knew we wanted to connect all the vertical edges together.

**49:34** · But that is not something that we can know always. So, that's why there is a more um general classes of techniques that are used for edge linking. They are usually called global method. So, the common global method for edge linking uses Hough transform.

**49:58** · So, if you consider a straight line in the image that is shown with equation y equals ax + b in which x and y are the coordinate system and a and b are the constant that uh specify the the linear equation. So, now let's say you basically transform this line into uh a transform domain.

**50:26** · And that transform domain uses parameters a and b to to represent the function. So, if you do that, uh any line in the original image will be transformed into a single point in the transform domain and any edge point is will be transformed into a line in the parameter space.

**50:53** · So, when you add up all these lines on points in the parameter space, what you end up with is that you end up with individual peaks in the parameter space or the transform space.

**51:09** · Each one of these peaks corresponds to a line in the image pixel. Of course, the procedure is a little bit more involved that what I described here, and there are different variations of Hough transform that are designed for detecting uh specific shapes in the images.

**51:31** · So, you can refer to to the original book or some other materials on Hough transform. But, for a quick example, here on top left we have this original area image of a an airport.

**51:47** · And to its right we have the result of Canny edge detector. So, if we use the result of the Canny edge detector and we calculate the Hough transform, uh what we do is what we end up with is in the parameter space is several peaks in each one of these peaks is corresponding to uh a straight line in the uh in the image. So, here is the result of only extracting two of these peaks.

**52:20** · And so, the two uh strongest peaks that we have in the parameter space.

**52:27** · If we uh align this with the image, you we see that these the two peaks in the Hough transform correspond to these uh these lines in the original image.

**52:40** · So, you are recommended to refer to the to the book to get a better idea about uh Hough transform.

### Image Thresholding

**52:49** · So, now that we saw all these techniques, it's the time to talk about image thresholding.

**52:56** · So, the general idea behind image thresholding is very simple. And you have seen minor examples of image thresholding uh in this lecture as well when we apply threshold on the values of the Laplacian or the values of the magnitude of the gradient.

**53:16** · So, the general idea behind image thresholding is that if we are given a threshold t, we want to partition the image into two regions.

**53:26** · One foreground or object and the other one is background.

**53:30** · So, the way it works is that for any uh pixel location, we compare the value of the image at that location with threshold t.

**53:39** · If the value is greater than the threshold, we assign one to the resulting image.

**53:46** · If the value for that location is smaller than or equal to the threshold, we assign a value of zero.

**53:55** · So, when this threshold is a constant that is applied to the entire image, it is called global thresholding. But, when the value of the threshold changes over the image, uh it is called variable thresholding.

**54:10** · So, when the value of threshold depends on the spatial coordinate x and y, it is usually called dynamic or adaptive thresholding. So, you can have multiple thresholds for an image, too. So, here is the mathematical representation of thresholding using two thresholds. So, we have t1, t2 sorry, t1 and t2. So, the resulting image if the original image at any location has a value greater than t2 would have a value of a.

**54:42** · If it's between t1 and t2 would have a value of b. And if it's less than t1 would have a value of c. So, I will show you a more example of how this thing works.

**54:54** · So, you can inspect the histogram of an image to have a better idea about the optimal threshold.

**55:01** · So, let's just say you are working with an image that has a histogram of this form. As you can see, you have two distinct uh ranges of intensity in your image. So, if you apply a threshold right between these two, you can divide the pixels of the image into two uh sets of pixels with intensities uh very similar to each other.

**55:30** · What about if you in your histogram you have three distinct uh ranges of intensity that all shown are with these like uh peaks here?

**55:42** · In that case, if you apply two threshold to that image, uh you can partition the original image into three uh different regions.

**55:56** · So, what happens if you have a noisy image? So, let's just see what happens there.

**56:03** · So, here on top left we have a noiseless 8-bit image. And as you can see, we have this region at the center with a constant intensity. And then we have some background also with a constant intensity. So, if we draw the histogram of this image, we have two peaks in the histogram.

**56:24** · This one is corresponding to the pixels inside the object, and this one is corresponding to the pixels in the background.

**56:34** · As you can see, you can easily define a threshold between these two. Let's say you put the threshold 127, and you're able to uh partition the image into uh two sets of pixels. One with uh intensity values of the background and one with the intensity value of the foreground or the object.

**56:58** · So, now let's say uh let's say we have a noisy image.

**57:02** · So, here is the a Gaussian noise with zero mean and a standard deviation of 10 intensity levels is added to the original image.

**57:13** · So, now let's see what happens to its histogram. As you can see, the histogram is not only two peaks anymore because when you add noise, you basically create uh random sets of intensity values.

**57:28** · But, even then, the the two peaks are still distinct uh and you are able to put use the same threshold 127 as before to classify or like segment the original image into two sets of pixels, each having similar intensities.

**57:48** · But, what if the level of noise is increased? So, here you see the original image, but this time is corrupted by additive Gaussian Gaussian noise with mean zero and a standard deviation of 50 intensity level.

**58:02** · So, now if you draw the histogram, you see that the histogram looks something like this. And as you can see, even though visually speaking when you take a look at this image, you're able to distinguish between the background and the foreground, but just by looking at the histogram, you cannot see the the two peaks anymore.

**58:26** · So, now the question becomes how you can apply thresholding based on the histogram on a noisy image.

**58:34** · Noise only is one one of the problem that you can have. What if you have uh non-uniform illumination or reflectance in your images? So, let's just say you have this original image. This is the noisy version uh as we saw in the previous slide. And here is the corresponding histogram. So, now let's let's say we have this intensity ramp in which the values for intensity changes from .2 to .6.

**59:02** · And this is the corresponding histogram for this intensity ramp.

**59:10** · So, now let's just say we uh element-wise multiply this intensity ramp with the original image.

**59:16** · So, after doing that, this is what we end up with. The areas to the left of the image are now a bit darker than the areas to its right.

**59:27** · So, now if you uh calculate the histogram, now you see that there are three peaks that are not very distinct in the histogram. So, how can you avoid uh segmentation error or thresholding error in such cases?

**59:44** · So, the main question that each one of these uh techniques need want to answer is that what is the optimal threshold that we can uh we can find for any specific

**1:00:00** · image because changing the threshold manually is one thing, but if you have an algorithm that can calculate the optimal uh threshold automatically, that is going to be the algorithm that you can use uh more commonly.

**1:00:20** · So, the first technique that I will discuss on image thresholding is called global image image thresholding.

**1:00:29** · So, when when the intensity distributions of object and background in the image uh are sufficiently distinct, it is possible to use a single threshold for the whole image.

**1:00:42** · So, the step for uh global image thresholding are as follows.

**1:00:47** · First, you select an initial estimate for the global threshold.

**1:00:53** · So, this estimate can be, for example, the average of all the intensity values of the image.

**1:01:00** · Then, you use this threshold to segment the image uh and based on this threshold, you produce two groups of pixels.

**1:01:10** · Group G1, which consists the pixels with intensity values greater than T, and group G2, which consists pixels with intensity values less than or equal to T.

**1:01:22** · So, now, you compute the average intensity values M1 and M2 for the pixels in G1 and G2, respectively.

**1:01:30** · And finally, you compute a new threshold value halfway between M1 and M2. So, the new threshold will be T equals 1/2 the summation of M1 and M2.

**1:01:43** · And now, you repeat steps two to four until the difference between the values of T in suc- successive iterations is a smaller than a predefined delta T.

**1:01:58** · So, as you can see, the the global image thresholding method is very straightforward. So, you you start with a an initial estimate for the global threshold. You do the thresholding. You end up with two groups of pixels.

**1:02:13** · Uh you calculate the average for each one of these two.

**1:02:17** · And then, uh you took you take the average of the averages to calculate the new threshold and you repeat the process.

**1:02:27** · The last step uh is basically is satisfied when a condition that you define yourself is satisfied. So, for example, if the difference between the values of the new threshold and the previous threshold is less than, for example, one, you can stop the procedure. So, let's just take a look at one example.

**1:02:54** · So, on the left, we have a noisy fingerprint image uh and that we want to uh segment into uh foreground and background. So, here, foreground is basically the fore- the fingerprint itself, and the background is basically the uh the gray background that we have.

**1:03:20** · So, in the middle, we have the histogram of this image. As you can see, we have two distinct uh ranges of intensity values.

**1:03:31** · So, what we end up doing here is that we start from the average value of the the original image, the whole image, and after three iterations, the global threshold uh is to be 125.

**1:03:50** · And this is the final result uh after you apply the uh global thresholding.

**1:03:59** · So, thresholding can be considered as a statistical decision theory problem.

**1:04:04** · So, the objective is to minimize the average error in assigning pixels to two or more groups of classes.

**1:04:12** · So, global image thresholding is a good technique, but it doesn't take it doesn't take into account the uh the variance of the uh groups of the pixels. So, basically, it doesn't take into account the differences between the the groups of pixels or the segments in the image.

**1:04:37** · So, the optimum global thresholding technique or Otsu's method tries to maximize the between-class variance, which measures the statistical discrimination between the classes.

**1:04:51** · This is uh conceptually equivalent to minimizing the in-class variance for each uh group or classes of pixels.

**1:05:00** · So, the derivation of the equations here is based on normalized histograms, and if you remember from before, the normalized histogram of an image of size M by N with intensity values changing from zero to L minus one is mentioned uh here. So, PI, which was the uh probability of intensity I is NI, basically the total number of pixels with intensity I divided by M multiplied by N.

**1:05:33** · So, M multiplied by N is the total number of pixels in the image.

**1:05:39** · And we know that the summation of all these probability values for the for all of the intensities would add up to one. So, now, let us see how Otsu's method uses normalized histogram to to to find an optimal uh threshold.

**1:06:00** · So, let's just assume we select a threshold T of K equals K. So, the threshold that we have is K.

**1:06:09** · And this threshold is something between zero and L minus one. And it's used to partition the image into two classes, C1 and C2.

**1:06:20** · So, in this segmentation, C1 consists of pixels with intensity values in the range zero and K, and C2 consists of pixels with intensity values in the range K plus one and L minus one.

**1:06:37** · So, now, the first thing that we need to do is to find the probability of each class.

**1:06:42** · And the probability of each class is done by summation. So, the probability of class one is the summation of all the probabilities for intensities changing from zero to K.

**1:06:55** · As you can see here, the pixels in class one change from zero to K for the intensity.

**1:07:02** · As for probability of class two, it's basically the summation of all the the probabilities for intensities changing from K plus one to L minus one.

**1:07:14** · Which, since the summation of all the uh probabilities would add up to one, this is equivalent to one minus P1 of K.

**1:07:24** · So, the next thing that we need to do is to find the mean intensity value for each class.

**1:07:30** · So, the mean intensity value for class one is one over the probability of the class multiplied by the summation of I PI, basically the intensity and the corresponding probability for that intensity.

**1:07:46** · The same can be done for the mean intensity of class two, which is equal to one over the probability of class two multiplied by the summation of the intensity with the probability of that intensity. And as you can see, for class one, since we only have intensities between zero and K, we do the summation between zero and K.

**1:08:11** · And for class two, we do the summation for intensity values K plus one and L minus one.

**1:08:19** · So, now, we can define the cumulative mean or average intensity up to level K using this equation, which is basically the summation for I changing from zero to K, I multiplied by PI.

**1:08:36** · And then, we have the average intensity for the entire image, which is basically the previous summation, but this time I can change from uh zero to L minus one. And as you can see here, we don't have any dependency on K. So, this is wrong. So, we have MK, but MG is not dependent on K. So, this should be MG.

**1:09:01** · This is wrong.

**1:09:03** · So, based on previous equations, uh it is obvious that P1M1 plus P2M2 equals MG.

**1:09:12** · And sum of P1 and P2 equals one. So, these are the things that you can easily verify using the uh previous equations.

**1:09:23** · So, now, we need to measure the effectiveness of threshold K.

**1:09:28** · And to do that, we define this parameter eta, which is basically the uh ratio between the between-class variance uh in the numerator and the global variance.

**1:09:45** · For the global variance, it is very straightforward. You basically calculate the summation of the intensity minus the average intensity of the which the the whole image squared multiplied by the probability for any intensity.

**1:10:02** · As for the between-class variance, since you have two classes, you basically do uh this summation uh for each one of these classes, and then you sum it together. So, we have P1 multiplied by M1 minus MG squared plus P2 multiplied by M2 minus MG squared.

**1:10:26** · So, you can manipulate this equation using the uh previous conclusions that we had, and then you can rewrite it in this form MG P1 minus M squared over P1 uh multiplied by 1 minus uh P1.

**1:10:45** · So, now if you look closely, some of the parameters were dependent on K or were like functions of K, which was the threshold. So, now if you consider that, this is the uh equation that we end up with for the between-class variance.

**1:11:07** · So, and this one eta K is basically the measure of effectiveness for any threshold K.

**1:11:15** · So, how to find the optimum threshold value?

**1:11:19** · Here we call it K star.

**1:11:21** · And the optimum threshold value is a threshold value that maximizes the between-class variance.

**1:11:30** · So, whatever threshold that maximizes this is the optimum uh threshold.

**1:11:39** · So, to find that, we change the value for K for all the possible intensity values, and for each one of them, we find the between-class variance, and whichever gave the maximum is going to be the optimum threshold. If multiple values of K maximize the between-class variance, what you do is basically you calculate the um the optimum K by taking the average of all those Ks that give us the maximum.

**1:12:10** · And finally, now that we found the threshold, we threshold the image as we saw before.

**1:12:18** · So, to summarize, the Otsu's method, first, we compute the normalized histogram of the input image, then we compute the cumulative sums P1 and P2 for uh all the values of K. We compute the cumulative means.

**1:12:38** · We compute the global mean and the global variance.

**1:12:42** · In a step five, we compute the between-class variance.

**1:12:46** · And in a step six, we find the optimum value for K. Here we call it K star that maximizes the between-class variance. If the maximum is not unique, we obtain K K star by averaging the values that result in maximum between-class variance.

**1:13:05** · And then we calculate the separability separability effectiveness uh as the ratio of the maximum between-class variance using K star as threshold and the global variance.

**1:13:20** · So, now let's take a look at one example to see the difference between global image thresholding and Otsu's method. So, on top left, we have the original image.

**1:13:30** · And on the top right, we have the histogram of the image. As you can see, uh there is no dis- no distinction between like the peaks of the histogram. So, just by looking at the histogram, it is not easy to find a proper threshold that can be used for thresholding this image.

**1:13:54** · On the bottom left is the result of uh applying the basic global thresholding method. As you can see, the threshold that it found is not able to uh distinguish the between the different intensity values of the image.

**1:14:13** · And the global method's threshold was 169.

**1:14:18** · On the other hand, Otsu's method, since it takes into account the in-between-class variance for measuring the effectiveness of the thresholding, it is able to do a much better job in thresholding the uh the image.

**1:14:37** · So, now let's see what happens when you are working with noisy images.

**1:14:41** · On the top left, you have the noisy image that we have seen before, and in the middle, we have its histogram, as you can see here.

**1:14:51** · There are no two distinct peaks that you can uh easily see and define a threshold. So, if you apply Otsu's method directly on this image, you can see that the segmentation is not very good so because of the excessive amount of noise, the result of the segmentation is not ideal. But now let's let's smooth the noisy image first by using a 5 by 5 averaging kernel.

**1:15:19** · And when we do that and we calculate the histogram, now you see that there are two distinct peaks that uh Otsu's method can use to basically find the optimum threshold.

**1:15:37** · And this is the result of thresholding using Otsu's method applied to the uh a smooth image.

**1:15:46** · So, chances of finding good threshold is higher if the histogram peaks are tall, narrow, and symmetric.

**1:15:55** · And they're separated by deep valley.

**1:15:58** · But what if uh only pixels on or near edges between the objects and the background are used to create a histogram?

**1:16:06** · So, you might say, why is the reason for doing that? So, let's just assume you are trying to find a segmentation or proper thresholding for an image in which the area that is occupied by the object is uh very small in comparison to the area that uh occupied by the background.

**1:16:28** · So, in in this example, as you can see, the area that is occupied by the object is comparable to the area that is occupied by the uh by the background, even though the area in the background is larger, and that is visible in the uh the area under the curve for each one of these individual peaks. But if the object was very small, in that case, the the peak for the object would be very small.

**1:16:55** · So, since uh Otsu's method doesn't take into account any of such information, what happens is that if you have uh a large gap between the the sizes of the areas occupied by the object and the background, the result of Otsu's method would be skewed, so it's not going to be ideal.

**1:17:18** · But you can remedy this by only considering the pixels that are uh very close to edges of the uh of the edge that is basically dividing uh the image and the sorry, dividing the object and the boundary.

**1:17:42** · So, if you only use pixels on or near edges between objects and the background, the resulting histogram would have peaks of approximately the same height.

**1:17:53** · Also, the probability that any of those pixels lies on an object would be approximately equal to the probability that it lies on the background.

**1:18:05** · So, this improves the symmetry of the histogram mode as well.

**1:18:09** · So, using pixels that satisfy some simple conditions based on either gradient or Laplacian uh tend to deepen the valleys between histogram peaks as well.

**1:18:21** · So, that's the idea behind improving global thresholding using edges.

**1:18:29** · So, for doing that, uh we need to follow a five-step process.

**1:18:36** · In the first step, we compute an edge image using magnitude of the gradient or absolute value of the Laplacian of the image f of x and y.

**1:18:45** · We uh specify a threshold value uh T, and then we threshold the uh the gradient image the edge image from step one using this threshold to produce a binary image GT of x and y.

**1:19:01** · So, using GT of x and y as a mask, we compute the histogram using only the pixels in the original image that correspond to the locations of GT of x and y that have uh values of one. So, basically, only pixels that are on or near edges are being considered to calculate histogram. Now, we use the histogram from step four to segment the image f of x and y to basically find a global threshold.

**1:19:32** · So, this global thresholding can be done either using basic global thresholding or Otsu's method.

**1:19:42** · So, this threshold is calculated and is applied to the uh whole image. So, the value for T that we used in the step two to basically segment the the edge image is usually chosen as a high percentile value.

**1:20:00** · So, few pixels in the gradient or Laplacian image will be used in the computation.

**1:20:06** · So, let's just take a look at one example.

**1:20:08** · So, on top left, we have a noisy image of uh background, a dark background, with a an object, very small object at the center. So, if you calculate the histogram, this is basically what we we see. We see a very large peak and intensity values of the background, right? And we don't see any peak associated with the intensity values of the the object.

**1:20:32** · And the reason for that is the area occupied by the background is much larger in comparison to the area occupied by the uh object.

**1:20:45** · So, now let's just directly apply Otsu's method to this image and see what we have. As you can see here, um the segmentation is not good at um good at all because as we said, uh since there is an asymmetry between the and the peaks in the histogram, uh Otsu's method is not able to provide a good threshold.

**1:21:15** · So, what do you think happened if we do some uh smoothing? Do you think it improves the result? Let's just see. So, the first image was noisy.

**1:21:24** · So, this image is the result of uh smoothing the original image using a 5 by 5 averaging kernel. And as you can see in the histogram, the histogram uh width is a bit narrower for the peak related to the background, but uh still you don't see any peaks for the pixels in the object, too. So, if you probably zoom in closely into this graph, you may see some peaks here, not necessarily in this image, but if you create something on your own.

**1:21:55** · But, uh for all practical intentions and purposes, the the peak for the object is basically nonexistent in comparison to the peak and the peak for the background. And now, if you apply thresholding, the result didn't improve that much.

**1:22:19** · But, now it's the time that we can improve this thresholding by using uh edge information. So, to do that, let's just see what happens. So, here we have the noisy image again and we have its histogram.

**1:22:36** · Image uh three is going to be is the mask image that is formed uh as the gradient magnitude image thresholded at uh 99.7%.

**1:22:50** · Image D is formed as the product of this image and uh image A.

**1:22:59** · And now, what we have is we have the histogram of the nonzero pixels in image D. So, basically, for the pixels that are on or near edges, uh we use those pixels to calculate the the histogram. Of course, for the pixels that are black, we didn't consider them at all.

**1:23:20** · So, now, using these two peaks that are now more visible, you can define the threshold and then based on that threshold, you can do the segmentation. As you can see, when you do it this way, you're able to distinguish between the background now it's shown all black and foreground now it's shown in all uh white.

**1:23:43** · So, let's just take a look at another example here.

**1:23:46** · On top left, we have this image uh image of some yeast cells and we want to be able to segment the the very bright core of these cells.

**1:23:58** · This is the histogram of the image. If we apply Otsu's method directly, this is what we get.

**1:24:05** · And since this is not what we actually look for, what we do is basically use the edge information.

**1:24:14** · So, we create a mask image by thresholding the absolute Laplacian image uh with a high percentile. And the percentile here was chosen at 99.5%.

**1:24:26** · And now, if we um use this mask image and apply it to the original image and then create uh a histogram, then roughly, you can see two like peaks. Of course, it is not uh very similar to the ideal case of having two narrow peaks, very symmetric with very deep valley between them, but uh still it is good enough to uh be used for our segmentation.

**1:24:56** · And finally, you see the result of uh segmentation using um a threshold that is calculated based on this uh histogram.

**1:25:10** · What if you want to use Otsu's method uh to derive more than one threshold?

**1:25:18** · So, the same equations that I discussed before can be extended to more than one threshold as well. I'm not going to go over them in detail. You can refer to the book.

**1:25:31** · But, generally speaking, you instead of calculating the in between variance between two classes, now you calculate the in between variance between three classes. And based on that, you uh decide on the optimum value for the threshold. So, here you can see a very obvious example of this being used.

**1:25:49** · We have this uh image of an iceberg and as you can see, we have a uh dark region as the background and we have two brighter intensity values here and here.

**1:26:06** · If you draw the histogram, there are three uh peaks or like intensity ranges uh visible that correspond to the background, this region, and this region, right? So, even visually, it is not very hard to see three different groups of uh intensity values.

**1:26:26** · If you apply a multi-threshold uh Otsu's method and do the segmentation, you can get uh this image.

**1:26:34** · Of course, you can see that the the result of the segmentation is not perfect. There you have regions in this area that are uh segmented as intensity values as uh other part of the part of the image.

**1:26:52** · For example, in this region, all of the pixels are shown with gray, but there are like some pixels that are shown uh as uh white. So, these are uh as a result of not taking into account the spatial information of the image and only working based on the histogram.

**1:27:12** · But, going into more detail is out of the scope of this course, so if you're interested, you can uh refer to the corresponding chapter of the book to see how we can eliminate such errors as well.

**1:27:29** · So, so far what we did was uh we found threshold that were global, meaning that the threshold was applied to the whole image.

**1:27:40** · What if you uh find threshold based on some local information? So, let's just say you have an image that is noisy or uh non-uniform illumination. So, you can what you can do is you can divide this image into several sections and for each section, you can find the threshold.

**1:28:00** · So, here you can see an example.

**1:28:02** · So, this is the noisy image, the noisy shaded image. As you can see here, the left side is a bit darker than the light right side. And if you uh calculate the histogram, you see that you see three peaks even though you only have like an object and the background, right? But, because of this non-uniform illumination, different patterns appear in the histogram.

**1:28:27** · So, if you uh do basic global thresholding method, this is the thresholding result that you get. So, there are regions in the object that are segmented as black and there are regions in the background that are segmented as white.

**1:28:43** · The global Otsu's method is not that much different.

**1:28:49** · But, if you divide this image into six sections and you find the thresholds for each one of these six sections, what you can do is that you can get to this uh segmentation result using local method.

**1:29:05** · So, basically, for each one of these section, you you find a different threshold and then you apply it to calculate the object and the background. And this is the uh combination of all those secret results. Even though it is not perfect, it is the still, um, improved from the the original, uh, also method.

**1:29:27** · There are some other cases that you can use variable or local thresholding.

**1:29:32** · Um, some common cases are uh, for reconstructing or thresholding text images that are captured by a scanner.

**1:29:44** · So, on top left you see text image that is corrupted by a spot shading.

**1:29:49** · Basically, uh, at the center you have a brighter appearance while on the corners you have uh, a darker appearance. If you apply global thresholding directly, this is the segmentation that you you get based on the result of the uh, result of applying the global threshold.

**1:30:10** · But now, if you use moving averages and you basically uh, scan your image line by line and you divide your image into uh, uh, several you go through the image line by line and you divide your images into partitions and for each partition you find the threshold.

**1:30:31** · And you do this, this is the result of the um, thresholding that you have. So, as you can see, it was able to adapt adapt to the uh, changes in the illumination of the image and was able to uh, segment the the image properly and extract the all the uh, written text.

**1:30:53** · Here is another example in which the image is corrupted by a sinusoidal shading. If you apply global thresholding, this is what you get. So, it is not able to get rid of the uh, the shading that corrupt the image. But if again you go line by line, you divide your image into multiple sections and you find uh, threshold for each one of these sections individually and then do it a step by step, this is the result that you get.

**1:31:27** · So, here I, um, I finished the talk on image segmentation. On the next lecture, I'm going to focus on color image processing. So, we will see fundamentals of color, color models and then um, how we can apply a lot of these techniques that we have learned so far on uh, color images.