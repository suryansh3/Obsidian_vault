---
title: "Digital Image Processing - Part 9 - Image Restoration In Frequency Domain"
source: "https://www.youtube.com/watch?v=xGN36BWK260&list=PL2mBI0yFsKk-p73KQ4iPdsi10hQC4Zd-0&index=9"
author:
  - "[[ASIP-Lab]]"
published: 2020-08-03
created: 2026-08-12
description: "Topics:08:07 Periodic Noise Reduction Using Frequency Domain Filtering28:48 Linear, Position Invariant Degradations36:25 Estimating the Degradation Function54:13 Inverse Filtering59:44 Minimum Me"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=xGN36BWK260)

Topics:  
08:07 Periodic Noise Reduction Using Frequency Domain Filtering  
28:48 Linear, Position Invariant Degradations  
36:25 Estimating the Degradation Function  
54:13 Inverse Filtering  
59:44 Minimum Mean Square Error (Wiener) Filtering  
1:12:19 Constrained Least Squares Filtering  
1:18:08 Geometric Mean Filter

## Transcript

**0:00** · Welcome to the ninth lecture of the digital image processing course. In this lecture, I'm going to go over image restoration in the frequency domain.

**0:12** · So, the topics that will be covered in this lecture are periodic noise reduction using frequency domain filtering. Then, I talk a little bit about linear position invariant degradation.

**0:24** · Then, estimating the degradation function.

**0:28** · And then, finally, I will introduce four different methods to restore images that are affected by degradation.

**0:36** · Inverse filtering, Wiener filtering, constrained least square filtering, and finally, geometric uh mean filter.

**0:45** · So, if you remember from last time, we said that we can create a mathematical model for image degradation and restoration.

**0:54** · So, we said that image degradation is modeled as an operator H, which together with an additive noise term for an input image f of xy generates the degraded image g of x and y.

**1:10** · So, now the problem of restoration is that given g of x and y and some knowledge about the operator H and some knowledge about the additive noise term, is it possible to restore the original image from the degraded version?

**1:31** · So, in this figure, you see both the degradation and restoration uh in the same figure. So, on the left, we have the degradation. We have this original image that we wanted to capture, but because of some uh limitations in imaging or some interference during the process of transmission, we end up with g of xy, which is the degraded version of the original image that we intended to capture.

**2:02** · So, now the question is that if we have some information about the degradation operator and the additive noise term, can we restore the original image using some restoration filters?

**2:17** · So, we said before that uh to model noise, we need to consider some parameters uh that are affected by uh let's say the the physics of the imaging sensor, for example, or the transmission of the image, or any other reason. So, there are different sources of noise. They usually appear during image acquisition and or transmission.

**2:46** · For example, in CCD cameras, light levels and sensor temperature are major factors.

**2:54** · We can have uh additive noise during transmission, too.

**2:59** · Uh mainly as the result of interference in the transmission channel. For example, in wireless transmission, uh lightening or other uh atmospheric disturbances cause noise.

**3:12** · So, last time we said that let's just only focus on an image that is only degraded by noise.

**3:19** · And then, we said that to be able to uh statistically model the behavior of the noise, it is best to consider each noise as having a probability distribution function.

**3:36** · So, based on this, we said that the noise component that is added to the image is an image itself with the same size as the input image. And then, we can simulate noise images by generating an array uh whose intensity values are random variables, random numbers with a specified uh PDF. We saw several examples of noise PDFs.

**4:01** · We saw Gaussian noise, Rayleigh noise, Erlang noise, uh exponential noise, uniform noise, and finally, we saw salt and pepper noise.

**4:15** · We said that for any uh noise PDF or in general for any PDF, we can uh define two important property. What One is the mean value and the other one is the is the variance. So, since the functions, the PDFs that we are using here are defined in the continuous domain, we use the uh equation, the continuous version of the equations for the mean and variance.

**4:41** · If you are working with uh probability density functions in the discrete uh domain, then you can use the summation version of these mean and variance equations.

**5:00** · So, we saw some examples of applying different types of noise to the images. On the left, we have this uh original image that has three different uh intensity values.

**5:14** · And then, if we apply the Gaussian noise at the at any uh spike in the histogram of the original image, now we have uh a Gaussian shape. The same can be seen for the Rayleigh noise and the Erlang noise.

**5:29** · Also, for the exponential noise, uniform noise, and for the salt and pepper noise. And if you remember from last lecture, we said that application of salt and pepper noise is a bit different than application of the other types of noise, because in other types of noise, uh you basically create a uh noise image, and then you just find the addition of the noise image and the original image.

**5:59** · As for the salt and pepper noise, you can think of the noise image as a mask uh in which depending on the value of the salt and pepper noise mask, you need to modify a specific pixels in the in the original image.

**6:17** · Then, we saw how we can uh restore images that are affected by different types of noises.

**6:25** · We saw mean filters, including arithmetic mean filter, geometric mean filter, harmonic mean filter, and contraharmonic mean filter.

**6:34** · We also saw order statistic filters, including median filter, min-max filter, midpoint filter, and alpha-trimmed um mean filter.

**6:45** · And finally, we saw adaptive filters, including adaptive local noise reduction filter, and adaptive uh median filter.

**6:54** · So, we said that mean filters are uh good for getting rid of uh Gaussian and uniform noise in general, but they are not performing very good when it comes to salt and pepper noise, especially since the two versions that can deal

**7:15** · with salt and pepper noise, uh the harmonic and contraharmonic filter, more specifically the contraharmonic filter, you need to specify the uh filter order in such a way that it can either reduce the salt noise or the pepper noise. On the other hand, order statistic filters are very good candidate of uh getting rid of uh impulse noise.

**7:42** · And finally, we saw that we can use adaptive filters in which uh depending on different locations of the pixels in the image, if we can uh adaptively tweak some parameters of the uh filter, we can get much better result as opposed to just uh use basic mean or order statistic filters.

### Periodic Noise Reduction Using Frequency Domain Filtering

**8:08** · As it was discussed previously, periodic noise uh can be analyzed and filtered using frequency domain filtering.

**8:15** · So, periodic noise appears as uh burst of energy or impulses of energy in the Fourier domain at locations that correspond to the frequencies of the periodic interference.

**8:29** · So, we saw three selective filters before, band reject filters, band pass filter, and notch filters.

**8:36** · So, notch filters are uh usually more used in image restoration, especially for getting rid of uh periodic noise.

**8:47** · Before I talk about notch filters in more detail, just as a reminder, take a look at these two functions, the sine function and the cosine function.

**9:00** · So, on the left are the sine and cosine function that are defined in the spatial domain.

**9:08** · As you can see, we have u0 and v0, basically as the frequencies uh of the repetition along the horizontal and vertical axis of the image. And if we calculate the Fourier transform uh of these two functions, what we see is that both of them are translated into two uh

**9:34** · impulse functions in the frequency domain, of course, with different amplitude, but nonetheless, uh any sine and cosine function in the signal domain is equivalent to having two uh impulse functions in the frequency domain.

**9:52** · So, that's how we can define the uh properties for the notch filters to remove this type of periodic noise.

**10:03** · So, notch reject filters are usually used for removing the periodic noise.

**10:09** · So, the transfer function for notch reject filters are usually created as a product of a few high-pass filters whose centers are translated to the centers of the notch.

**10:23** · So, this was a mouthful. So, let's just see how it looks like in mathematical term.

**10:29** · So, H of NR is the transfer function of the noise reject filter in the frequency domain. As you can see, it's dependent on values variables U and V.

**10:43** · Equals, this is the product sign.

**10:46** · Product for K changing from 1 to Q of HK U and V and H minus K U and V.

**10:56** · Where HK and H minus minus K are high-pass filters with centers at locations UK, VK and negative UK, negative VK respectively.

**11:10** · So, it means that if you plan to remove some frequencies uh frequencies UK, VK uh since we are working with periodic noise definitely we will have uh uh symmetric representation of this frequency uh with respect to the origin of the frequency domain. So, we have UK and VK.

**11:39** · We have an impulse in this frequency and also we have an impulse in the uh frequency negative UK and negative VK.

**11:48** · So, that's why we have both of these thing multiplied together.

**11:52** · So, frequency domain filters, as we have seen before, are symmetric about the center of the frequency rectangle.

**11:59** · This is the direct property that came from the definition of the discrete Fourier transform that the discrete Fourier transform is periodic and the center uh uh and center for rotation or center for symmetry is the origin.

**12:18** · So, because of this the notches that we specify are specified as symmetric pairs.

**12:25** · So, uh now that we have this, we can define the center distance for the high-pass filters using these two equations. So, on the one on top is for uh difference from

**12:42** · center for a uh for a for an impulse that is located at location UK and VK and the bottom one is the the center distance from the origin for the frequency that is located at negative UK and negative uh VK. So, now let's see how we can combine these to create some sample and notch reject filters.

**13:10** · So, here you can see an example uh of a Butterworth notch reject filter of order N with three notch pairs.

**13:19** · So, you remember any single one of these was the uh generic Butterworth uh high-pass filter. So, now since we want to have a high-pass filter uh H uh subscript K and another one H subscript negative K we multiply these two together.

**13:44** · And since we want to get rid of let's say three different periodic noise, then we have to calculate the uh product of these three different filters. One thing that you should note is that the D0K is the same for each pair, but can be different for different pairs.

**14:05** · And if you have a notch reject filter uh creating a notch pass filter is very straightforward. So, the transfer function of a notch pass filter there should be a V here. So, H of NP of U and V equals 1 minus H of NR. So, the transfer function function of the notch pass filter equals 1 minus the transfer function of the notch reject filter.

**14:34** · So, here you see three different examples uh notch notch reject filters.

**14:41** · Uh of course, in these examples there are only one frequency component that we want to uh eliminate. And again, one frequency component in the spatial domain is represented as two uh impulses in the frequency domain, two symmetric uh impulses uh in the frequency domain which are symmetric with respect to the uh origin of the frequency domain.

**15:09** · So, this is an example of an ideal notch reject filter. This is an example of a Gaussian notch reject filter and this one is an example of a Butterworth notch reject filter. And if you remember, we when we change the value of N, we can make the Butterworth filter to look more like a Gaussian or an ideal uh filter.

**15:33** · So, let's just see how it works in action. Again, this is an image that we have seen probably four, five times uh up until now. So, on the top left we have an image from the moon surface that is corrupted by a sinusoidal interference pattern.

**15:52** · If you want to get rid of this uh interference pattern in the spatial domain, we basically have to divide the filter that can be applied to the whole image. And since this interference appears in all the pixels of the image, it is going to be very hard to get rid of.

**16:09** · But when we convert this into a frequency domain uh what we see is that this interference pattern shows itself as these two bright dots uh that you can see here. They are shown with these two arrows. So, now to get rid of these, what we can do is that we can design a notch reject filter in which it is zero at the location of these two spikes.

**16:42** · And it is one uh at any other location.

**16:46** · So, this is the filter that we can design.

**16:49** · And now if we element-wise multiply this mask or this filter with the uh Fourier transform of the image what we can get is the interference and or noise uh free uh image that we want to. And then if we subtract the original image and this one together, we can get an image that shows the interference pattern only.

**17:19** · Let's just take a look at another one.

**17:23** · Here on top left we have an image uh and basically a radar image from the uh from Florida and Gulf of Mexico. And as you can see, because of the imaging system that we have used uh we see horizontal scan lines appear all over the image.

**17:44** · So, in the frequency domain, if we convert it into frequency domain and uh center it, this is the spectrum of the Fourier domain. So, now we can design a rectangular notch filter that basically is uh zero in these two regions and it's one otherwise. And if we element-wise multiply this with the Fourier transform, not necessarily the spectrum, but also the phase, too.

**18:14** · Then what we get is this version of the image which in which a lot of the horizontal scan lines are eliminated. Of course, you see that there are still some interference that uh appear in the result as a result of maybe uh not perfect design of the filter or uh what if there are more interference pattern and we are only getting rid of some of them.

**18:45** · But in any case this image is uh uh containing less interference than the original one. And again, if you subtract this from the original image, we can get an image of the interference pattern.

**19:00** · So, in all the previous examples, the interference patterns were very easy to identify and characterize in the frequency domain. But what if we have multiple interference pattern?

**19:11** · How to ensure that we uh remove less of the image information during the filtering process?

**19:20** · So, to make sure that this is the case, we require to do optimization of the filter parameters.

**19:27** · So, to achieve this, let's start with the notch pass filter to extract the interference pattern.

**19:34** · So, this is represented in the frequency domain and uh spatial domain as these two equations. So, in the frequency domain, N of U and V equals H of NP basically the transfer function of the notch pass filter element-wise multiplied by G of U and v.

**19:53** · To get the spatial the domain representation of this equation, what we need to do is that we need to calculate the inverse discrete Fourier transform of the of both sides of the equation. So, in that case n of x and y, the spatial representation of the interference pattern, equals inverse discrete Fourier transform of h and p u and v multiplied by g of u and v.

**20:21** · So, now since we assume that the interference is additive, we can estimate the interference pattern interference free image as f hat of x and y equals g of x and y minus n of x and y.

**20:39** · So, now what we need to do is that we said we want to uh change filter parameters and how it affects the image. To model this, uh and to account for uh the effects of incomplete components that are not present in the estimate of noise, we use a weighted or modulated estimate in this form.

**21:02** · So, the weighted form is f hat of x and y equals g of x and y minus a weight function multiplied by the the interference component.

**21:17** · So, uh optimum uh optimum notch filtering aims to minimize the local variance of the restored image. You might ask, why do we care about the local variance of the restored image?

**21:31** · So, what is the effect of interference in the image? If you are in a region that is uh having uh constant or like close to constant uh intensity values, because of the interference, what happened is that the variance between the intensities of the pixels in that neighborhood would uh definitely increase.

**21:52** · So, now we want to modify these weights in such a way that the final result has minimum local variance to basically be able to get rid of the interference uh better.

**22:07** · So, to do that, we make two assumptions.

**22:11** · First, we assume a neighborhood s of xy of odd size m by n that is centered uh on location x and y, and also we assume that the weight in the neighborhood is constant and it is the weight at the center pixel.

**22:29** · So, this is a simplifying assumption because if uh we assume the weight to be changing even in the neighborhood, the equations are going to be much more complicated, which we don't want to get into.

**22:43** · So, now based on these two assumptions, we can write the equation for the variance of the restored image at location x and y and in the neighborhood sxy uh by following the definition of the variance.

**22:57** · So, sigma squared equals 1 over mn, basically 1 over the total number of pixels in the image equals the summation of f hat of rc minus f hat bar.

**23:14** · And this subtraction is raised to power two.

**23:18** · And rc are all the pixels uh inside the neighborhood.

**23:23** · And f hat bar is uh the the average of the pixels, the average of the restored image in the neighborhood. So, now the only thing that we need to do is that we need to replace this equation uh using the equation that we had uh at the beginning of this slide. So, f hat rc equals g of rc minus w x and y multiplied by n r and c.

**23:54** · And the reason that we use w x and y and not w r and c is that we said uh we assume the weight is constant and it is the weight at the center pixel, right?

**24:04** · So, it's only a single value for the center pixel.

**24:08** · And we can uh do the same for the average value of the restored image in the neighborhood, too.

**24:15** · So, in that case, it is going to be reduced to g bar, basically the average value of the degraded image in the neighborhood minus w x and y. Again, this is the constant uh weight that is only considered for the center pixel multiplied by n bar, which is the av- average of the noise component in the uh rectangular neighborhood that we have.

**24:41** · And again, the bar symbol is to show the average of the corresponding parameter in the neighborhood. So, now that we have this equation for the variance, we can uh achieve our goal, which was to minimize the variance with respect to the w.

**24:58** · Right? So, so the w is the variable here and we want to minimize the variance with respect to it.

**25:07** · So, to do that, we take the derivative of the variance with respect to w and we make it equal to zero.

**25:19** · So, the partial derivative of sigma squared of x and y over sigma w uh x and y should be equal to zero. So, if we calculate this derivative using this equation and we equal it to zero, then the result for the w of x and y,

**25:41** · the weight for the center pixel is going to be the average of the multiplication of g and n minus the average of g multiplied by the average of n over uh n squared bar, basically the noise component squared and then taking the average minus n bar squared, basically the noise component uh taking the average and and taking the average to uh power two.

**26:13** · Which means that for every pixel x and y, this weight is computed and then using the first equation in the uh previous slide to basically create the interference uh free uh image.

**26:32** · So, now let's take a look at one example. On the top left, we have an image of the Martian train with some complex semi semi-periodic interference pattern.

**26:44** · So, if we calculate the Fourier transform and then we center it and calculate the spectrum, this is the image that we see.

**26:54** · As you can see, we have a lot of uh impulse-like uh spikes in the frequency domain. So, just by taking a look at this, we cannot say, "Okay, which one of these is the uh interference, which one is part of the original data?"

**27:14** · So, an- another thing is that it is not always uh useful to uh center the Fourier spectrum or the uh the Fourier transform. And that is actually what is uh sometimes common uh in practice. So, this is the uncentered centered Fourier spectrum and then an expert designed the Fourier spectrum of the interference to look something like this.

**27:41** · As you can see, there are a few dots here and there uh that is uh designed or derived based on the judgment of the expert in the field.

**27:53** · So, now if we uh calculate the uh inverse of this, we can get uh this pattern, this especially interference pattern.

**28:08** · Uh and by optimizing the parameters for individual pixels, what we get is this uh restored image. And as you can see, uh a lot of the interference that was present in the first image, they are gone in the restored image. But at the same time, you realize that going from this image to this one was not as a straightforward as designing uh a notch reject filter and just applying it to the image.

**28:43** · There are more uh steps involved. So, So, now that we saw how we can get rid of the periodic interference in the images, uh let's just talk about linear position invariant degradations, which is a more general consideration uh of the degradation and restoration modeling.

### Linear, Position Invariant Degradations

**29:06** · So, if you remember before, we said that we uh considered the degradation operator as a linear position invariant degradation. But what the what does it mean?

**29:19** · So, the input-output relationship for this uh degradation process can be shown as g of x and y equals h applied to f of x and y plus uh n of x and y.

**29:36** · So, now the question becomes, how we apply h to f of x and y?

**29:42** · And the answer to that is not uh very simple. It depends on the type of the operator that you have. So, let's say if the operator is uh um a power of two, right?

**29:55** · It's going to be totally different than if it was uh a linear function, right?

**30:03** · So, for uh linear and position invariant degradation, the answer is very straightforward. So, let's just see what uh does linear and position invariant mean. So, you have seen examples of linear operators before.

**30:20** · Uh we know we say that operator H is linear if it satisfied the additivity and homogeneity properties as follows.

**30:30** · So, H of AF1 + BF2 should equal H of A H of F1 + B H of F2. So, this is a combination of the two properties. So, we have additivity and we have homogeneity for operator H. So, this is something that we have seen before.

**30:50** · But, this is a still not uh not enough for us to get to a simpler uh approach to show the relationship between uh input and output in a degradation process.

**31:06** · The other important property uh for the operator is that it should be position invariant.

**31:12** · So, what does it mean to be position invariant?

**31:17** · So, before that, let's just um ask it a little bit differently. What does it mean for an operator or for a system to be time invariant?

**31:28** · So, a system is said to be time invariant uh when its output to a given input does not depend on the time that you apply the input. So, if you apply the input at time T1, it should get give you a response uh R1, let's say. But, if you wait 2 days and you apply the exact same input, the output should be exactly the same.

**31:57** · So, this is for time invariant systems.

**32:01** · Uh for position invariant system, it's basically the same thing. The only difference here, as opposed to time invariant, is that for time invariant systems, the variable was time. But, in images, what we have as the variable is the spatial uh location, right? So, that's why we call it position invariant.

**32:23** · So, it means that if we apply uh H to function F, we should get G.

**32:32** · But, if we apply H to a shifted version of function F, we should get G with exactly the same amount of shift along horizontal or vertical directions.

**32:45** · So, in mathematically, uh this is shown like this equation.

**32:50** · H applied to F of X minus alpha and Y minus beta, basically F of uh X and Y that is shifted horizontally to location alpha and vertically to location beta is equal to G of X minus alpha, Y minus beta, basically G of X and Y that is horizontally shifted to location alpha and vertically shifted to location beta.

**33:17** · So, that's what we mean by position invariant. If you shift the input, you should get get um a shifted output, but the form of the function should not change. So, that is what is called the position invariant.

**33:30** · So, now uh let's say we have an operator H that is both linear and position invariant.

**33:39** · What are the implic- implications of such operator?

**33:44** · So, it can be proven and it is uh proven in the textbook. So, I highly suggest you go over the the proof yourself. So, it can be proven that if H is linear and position invariant, then the degradation in the spatial domain can be represented by using convolution.

**34:04** · So, this is a huge relief because before, how H is applied to F, we had no idea. There could be uh infinitely many ways that H can be applied to F.

**34:20** · But, now if H is linear and position invariant, it can be modeled the degradation can be modeled as uh a convolution operator.

**34:32** · In which in this equation, H of X and Y is called either the impulse response or the point spread function of the degradation operator.

**34:44** · So, why is it called the impulse response?

**34:48** · Because it means that if you have the uh the system and you give it an impulse function as the input, whatever you get at the output is going to be H of X X and Y.

**35:02** · Uh in the Fourier domain, uh we have this uh equivalent equation G of U and V equals H of U and V element wise multiplied by F of U and V plus N of U and V. So, this is basically using the convolution theorem that we discussed extensively uh in last chapter.

**35:27** · So, now the goal of image restoration is to estimate the degradation operator.

**35:33** · And here, for simplicity, we only focus on linear position invariant degradation operators.

**35:43** · So, there are definitely uh other types of degradation in which they are not linear or position invariant. These are not the topics of this uh this course.

**35:55** · One important thing that you should know is that we don't use padding for frequency domain restoration here uh because what we have here is the degraded image.

**36:06** · Padding is only effective if they are applied to the image before degradation, which is pointless here because if we had access to the original image uh beforehand, right? Before degradation, then what was the point of restoration?

### Estimating the Degradation Function

**36:25** · So, now let's just see how we can uh estimate the degradation function. Basically, how we can estimate the H of X and Y or the capital H of U and V.

**36:39** · Uh since the degradation is modeled as convolution, image restoration is usually called uh image deconvolution.

**36:50** · Basically, reversing the effect of convolution.

**36:54** · There are three ways to estimate the degradation function.

**36:57** · Uh one way is for uh is by observing the image.

**37:02** · Uh the other one is by doing experimentations, and finally, we can do mathematical modeling.

**37:09** · So, there is another way for uh calling the image restoration.

**37:14** · Uh since the process of image restoration uh is done by an estimated degradation function, it is also commonly called as blind deconvolution.

**37:25** · Uh So, to see how this approach work, let's just only focus uh on a model with only degradation without any noise component. So, we will introduce later on how we can have both degradation and noise. But, for now, let's just only focus on the cases that we have degradation without any noise.

**37:50** · So, in this case, G of U and V equals H of U and V element wise multiplied by F of U and V.

**37:59** · So, now let's just see uh how we can do degradation estimation by image observation.

**38:06** · observation.

**38:07** · So, without any knowledge of the degradation function, we still can gather some information from the image itself.

**38:16** · So, for example, if the image is blurred or if the image is as a result of uh shake uh in the camera, right?

**38:24** · So, there are still some useful information in the image even though we don't actually know what was the degradation function.

**38:34** · So, using these information, we can get a good estimate of the degradation function. For example, if the image is blurred, we can inspect a small section and which contains both image features and background.

**38:49** · Right? So, since the image should contain a specific features, we can say, "Okay, we have G of S as the observed section of the image, and we have FS uh F hat of S X and Y as the expected res- restored section."

**39:08** · So, now if we can uh create these two uh values, then the the transfer function of uh the degradation uh for that a specific uh patch or a specific section of the image, it's going to be G GS of U and V F hat S of U and V.

**39:34** · So, let's just say you are expecting to have very sharp edges in your image, but what you get is a blurred version of that. So, by inspecting those sharp edges and your expectation, you can estimate how much blurring you have in in your image. And based on that, you can define the degradation function.

**39:55** · So, based on the assumption of linear position invariant degradation, you can construct the function h of u and v on a larger scale that basically can be applied to the whole image, but having the basic shape as the transfer function of the degradation in a small section of the image. So, that is one way of estimating the degradation function by image observation.

**40:22** · Another way is by experimentation.

**40:25** · So, if you have access to the equipment that captured the image or a similar equipment uh to one that captured the image, what we can do is that we can use that equipment to estimate the degradation function.

**40:42** · So, you might ask how?

**40:44** · Remember that we said the degradation operator is usually called point spread function or an impulse response.

**40:53** · So, that means that using the equation that we have, if we can simulate an impulse, basically a broad bright dot of light, and we pass it to the equipment, and we image it, then what we get at the output is going to be the impulse response or the representation of the degradation operator.

**41:19** · So, mathematically speaking, this can be shown using this equation. h of u and v equals g of u and v over a, in which a is a constant and is the Fourier transform of the of an impulse with strength a.

**41:38** · And g of u and v is basically the result of the application or the passing of this impulse function to the equipment.

**41:49** · So, let's just take a look at one example.

**41:52** · Uh here on the left, we want to basically estimate the degradation of an operator that blurs the blurs the image. So, on the left, we have an impulse of light.

**42:06** · Uh and on the right, we have the the degraded impulse. So, since this impulse in the frequency domain is a constant value, if we calculate the frequency domain of this response, and then we calculate this division, what we have is a good estimate of the degradation function.

**42:32** · The third way for estimating the degradation function is by mathematical modeling.

**42:40** · So, for estimation by mathematical modeling, we take into account the physical properties of the degradation operator. For example, when you capture aerial images, um you can use physical characteristics of the air turbulence, and based on that, you can estimate the degradation in aerial photos. So, of course, you are not going to be asked to derive these equations.

**43:11** · These are just the given, but the way that these equations are derived is by taking into account the physical characteristic of the phenomena that degrade the image.

**43:24** · So, this degradation function, uh if you look closely, it's h of u and v equals e to the negative k u squared plus v squared to the power 5 over 6.

**43:39** · In which k is a constant that depends on the nature of the turbulence. And if you look closely, you see that this function is very similar to uh a Gaussian low pass uh transfer function, except with the 5 over 6 uh power that you have.

**43:59** · But overall, it is a Gaussian function. So, and we have already seen before that a Gaussian function it is a smoothing It's a smoothing filter. And if you remember, it was from one of the homeworks that we said Gaussian uh smoothing is a better uh estimate of blurring rather than box filtering.

**44:26** · But in any way, when we change variable k, we can simulate blurring of aerial images with different amount of blurring. So, let's just take a look at one example.

**44:39** · In the top left corner, uh we have an aerial image without any uh visible turbulence or blurring.

**44:48** · On the top right corner, you see severe tur- turbulence as a result of having a value for k of 0.225.

**44:59** · Bottom left is uh with mild blurring or turbulence with a value of k being 0.001.

**45:11** · And then finally, for the last image, we have low turbulence with a value of k being 0.1.

**45:17** · Sorry, 0.00025.

**45:21** · As you can see, when you decrease the value of k, you basically decrease the amount of blurring that you see in these type of aerial images.

**45:32** · So, let's just take uh take a look at another example.

**45:38** · So, this is for you to see the general approach for uh such modeling. So, here what we want to do is that we want to drive the equations for modeling blurring in images as a result of motion uh between the image and uh sensor during image acquisition.

**45:59** · So, here we want to model image f of x and y going through a planar motion.

**46:06** · And for this modeling, we assume x0 of t and y0 of t uh the time varying components of the motion in x and y directions.

**46:20** · So, we assume that the shutter opening and closing is instantaneous.

**46:25** · So, what we have is that the shutter opens instantaneously.

**46:30** · We have a period of time, a duration of time in which um the image acquisition is done.

**46:37** · During that time, we have motion, and then finally, the the shutter closes.

**46:43** · Again, the shutter closing happened instantaneously, but between these two, we have a duration t in which uh we call it duration of the exposure.

**46:53** · So, the captured image at any point is the integral of the exposure during the time that the shutter is open.

**47:01** · So, if capital t is the duration of the exposure, we can write the equation for the captured image like this. So, g of x and y equals the integral from 0 to t. So, the integral is calculated over time of f of x minus x0t and y minus y0t dt.

**47:26** · So, if x0t and y0t are 0, this is going to be the integral from 0 to t of f of x and y, which is basically the image without any uh motion blur. But if you have any other value for x0 and y0, then you have motion blur in the image that you want to capture. So, now the aim is to estimate the degradation function by mathematical modeling.

**47:55** · So, the way to do it is we can do it in the Fourier domain.

**48:01** · So, let's just calculate the discrete Fourier transform of the both sides of this equation.

**48:08** · So, we have g of u and v equals double integral from negative infinity to positive infinity of g of x and y e to the negative j 2 pi ux plus vy.

**48:20** · Uh and the integrals are calculated over variable x and y.

**48:25** · So, now we had the previous equation for g of x and y, which was the integral from 0 to t f of x minus x0t y minus y0t uh over variable t.

**48:40** · So, now we have three integrals that we need to calculate.

**48:45** · This complex exponential function is not dependent on variable t.

**48:51** · Uh So, what we can do is that we can switch the order of these integrals. So, we calculate the integral over variable t at last, and then what we do is that we calculate these two integrals over x and y for the shifted version of the function f, f of x minus x0t and y minus y0t.

**49:19** · So, if you remember from the properties of the Fourier transform calculation, if we have a shifted version of the function in the spatial domain, it shows itself as uh a complex exponential function in in frequency domain with those exact amount of shift uh presented as the in the power of this complex exponential function.

**49:46** · So, now after doing the calculation and using that property, we have the integral from 0 to t of f of u and v e to the negative j 2 pi u x 0 t plus v y 0 t.

**50:01** · And the this integral is calculated over variable t.

**50:05** · So, now since this integral is over variable t and f of u and v uh is not a function of t, we you can take it out of the integral. So, g of u and v is going to be f of u and v multiplied by this integral.

**50:22** · So, if you remember, we said that now we only focus on the cases that we only have degradation without any noise, right? So, this function this integral is basically the h of u and v, the estimation of the degradation function.

**50:40** · So, h of u and v is going to be the integral from 0 to t e to the negative j 2 pi u x 0 t plus v y 0 t.

**50:50** · And the integral is calculated over variable t. So, now this is the general equation for for the motion, right? We still don't know what are the functions x 0 t and y 0 t.

**51:05** · So, if the motion variables x 0 t and y 0 t are known, then you can replace it into the equation and then you do the integral to calculate the uh exact function for h of u and v. For example, if we assume that we have a linear motion with rates x 0 of t equals a t over capital t and y 0 of t equals b t over capital t

**51:34** · with a and b being uh uh some variables like some constant and capital t is the duration of the exposure.

**51:44** · And each one of these is calculated uh x 0 t is in x direction and y 0 t is in y direction.

**51:53** · If we replace this in the equation for h of u and v, we get this function capital t over pi u a plus v b sine of pi u a plus v b multiplied by e to the negative j pi u a plus uh v b. If you look closely in this equation at this equation, you realize that this part is basically a uh a sync function. Of course, with a different constant, right?

**52:24** · But nonetheless, it's a sync function. And this one it is as a result of a shift uh in the integral. So, if you remember, we said that uh when we were taking the integral of a a box function from negative uh w over 2 to positive w over 2, we didn't have any shift in the uh Fourier transform, but if we had a box function that was non-zero from 0 to w, then we had a shift.

**52:56** · So, basically, you can think of it that way. Of course, uh depending on the different uh variables that we can we have for x 0 and y 0, this function is different. So, uh I just wanted to point out that this function even though it looks very complex, it is not that complex. You have seen examples of it uh before.

**53:23** · This function is uh in continuous domain.

**53:27** · So, to create um the discrete version of this function, what you need to do is that you sample this function at location u changing from 0 to m minus 1 and v changing from 0 to n minus 1.

**53:43** · So, here you see an example of application of this degradation function into an image. So, on the left, you have the original image without any motion blur. And on the right, you have the motion blurred image uh in which a and b are equal and equal to 0.1 and t the capital t the duration of exposure is uh is 1.

### Inverse Filtering

**54:14** · So, let us talk about different ways that uh we can use those estimations that we had to basically restore the image.

**54:25** · So, the simplest approach is inverse filtering, which means that to obtain the uh restored image, the degraded image is element-wise divided by the estimated degrade degradation transfer function in the frequency domain.

**54:43** · So, let's just see how it looks.

**54:45** · So, if you remember, we had g of u and v to be equal h of u and v multiplied by f of u and v plus uh n of u and v, right?

**54:56** · So, inverse filtering says that f hat of u and v equals g of u and v element-wise divided by h of u and v.

**55:06** · So, now if we replace g of u and v with its uh equation, now we have h of u and v f of u and v mhm plus n of u and v over uh h of u and v.

**55:23** · So, now in the first term, we have h of u and v multiplied by f of u and v divided by h of u and v. So, h of u and v will be canceled out. So, we have f of u and v plus n of u and v over h of u and v.

**55:39** · So, this is this seems very simple, right? Especially if you don't have any noise component.

**55:45** · So, if you don't have any noise component, this gives you the uh straightforward answer without any other consideration.

**55:53** · But what if we have noise, right? And that is very common, right?

**56:02** · So, then what we can do is that if we know the degradation function, we cannot recover the original image since we don't know the uh the Fourier transform of the noise component, right?

**56:19** · We may know some properties of the noise component, but we don't know the exact noise component.

**56:27** · Also, if the degradation function has zero or small values, then uh the ratio n of u and v over h of u and v will dominate the term f of u and v, right? So, these are the problems with uh inverse filtering.

**56:47** · So, let's just take a look at one example.

**56:52** · So, on the top left, we have uh we plan to restore uh an image that we saw before a blurred aerial image.

**57:04** · Uh but what we do here is that we just simply calculate the inverse Fourier transform.

**57:11** · Sorry, we calculate inverse filtering, right?

**57:14** · So, this is the resulting image that we get because that blurred image also contained a little bit of noise. Uh the the noise component uh in addition to having small values for the degradation function as mentioned here, basically dominate the the original image.

**57:38** · So, what we can do to reduce the effect of zero or small values uh in the degradation function is to limit the filter frequencies to values near the origin of the frequency domain.

**57:52** · So, basically, we apply a filter uh before calculating the inverse discrete Fourier transform into the result of inverse filtering.

**58:06** · So, on top left corner, we have the result of restoration without any filtering. Basically, here says with foot full filter, that means that we consider the whole frequency domain for calculating the inverse discrete Fourier transform. On the top right corner, we see the result with uh h or the estimate of the degradation function cut off outside a radius of 40 pixels.

**58:35** · This one is with the result uh is the result with h cut off outside a radius of 70 pixels. And finally, the last one is the result with h cut off outside a radius of uh 85. So, there is a sweetest spot that you can choose to basically make sure that the the result of inverse filtering is uh is good, right?

**59:10** · Uh so, basically, if you increase this uh the the last uh cut off frequency, you basically get the the image on top left corner.

**59:22** · But in any case, inverse filtering is a very straightforward and direct way for the image restoration. And because of that, since there is no optimization, um you need to do manual uh change of parameters or manual filtering to uh get the result that you want.

### Minimum Mean Square Error (Wiener) Filtering

**59:45** · So now, because we didn't have any control over the parameters of the inverse filtering, uh let's just see how we can introduce some optimization into the process to make sure that the result that we get uh is optimal in some sense.

**1:00:03** · So, as I said, the inverse filtering approach does not have any exple- explicit consideration for the noise in the process of restoration, right?

**1:00:14** · We didn't use any properties of the noise.

**1:00:17** · On the other hand, the minimum mean square error or the Wiener filtering approach consider both the image and the noise as random variables, and it aims to find the restored image with minimum mean square error with the uh uncorrupted image.

**1:00:36** · So, uh if you look closely, this is very similar to what we had for uh restoration of images corrupted by periodic noise when we decided when we wanted to do uh minimization of the variance. So, this is uh kind of similar to that.

**1:00:57** · So, the error metric uh that we define here is uh e e to the power two, which equals the capital E or the expected value of f minus f hat squared. So, f e is the uncorrupted image, and f hat is the estimate, right?

**1:01:19** · So, from the beginning, you see that okay, so to have a good estimate, we need to have the the original image, right? So, that kind of defeats the purpose. But, these are the initial steps to drive the final equation.

**1:01:36** · So, the noise and image are assumed uncorrelated, who and either one of them uh has zero mean.

**1:01:44** · Usually, usually, the noise component is considered to have zero mean, and the intensity levels in the estimate are a linear function of the levels in the degraded image. So, these are the assumptions that we have for devising the Wiener filtering. So now, if you put all these assumptions together, you see this uh scary equation.

**1:02:09** · Uh of course, you are not going to be asked to drive this, right?

**1:02:15** · Um because there are more steps in uh driving this equation, which is basically beyond the scope of this course. Just uh take this equation from me, and then try to understand it as uh best as possible. So, considering all these assumptions, the restored image can be represented in the following form.

**1:02:37** · So, uh as you can see, we have h a star, which is basically the the conjugate complex conjugate version of the h. We have sf, we have sn, which you don't know what they are.

**1:02:57** · So, h a star is the complex conjugate of h of u and v.

**1:03:01** · Uh absolute value of h squared is basically the multiplication element wise multiplication of h a star and h, or in other words, this is the spectrum of the uh sorry, it is it is uh the the power, I believe, of the degradation function in the frequency domain. sn is the power spectrum of the noise, and sf is the power spectrum of the undegraded image.

**1:03:35** · So, you see we have these three uh components.

**1:03:40** · One is the power spectrum of the degradation function, power spectrum of the noise, and power spectrum of the undegraded image, right? So, now considering this, it is a bit uh more easier to understand this equation.

**1:03:56** · So, let's just say we have a f hat of u and v, and let's just consider the final result. So, if I consider uh basically, put this one, do the multiplication, put it here, f hat of uh u and v equals g of u and v divided by h of u and v, right? So, if I go back a little bit, f hat of u and v equals g of u and v divided by uh h of u and v, right?

**1:04:27** · So, as you can see, this part is basically the inverse filtering itself. But, we have this additional term that is going to be multiplied with the inverse filtering. So, in some sense, this is an additional uh transfer function that can act as a filter on the inverse filtering, right?

**1:04:47** · But, since uh this equation is derived based on some optimization, you can say that the uh the result of that optimization is basically to control how uh this filtering is is performed.

**1:05:06** · So, if the noise is zero, the Wiener filtering reduces to simple inverse filtering. So, if the noise is zero, basically means that the power of the noise in the frequency domain is going to be zero, then sn over sf is zero, then h squared over h squared is going to be one, and f hat is going to be reduced to g over h, right?

**1:05:31** · But, that is probably not the case, right? Because as we said before, if the noise was zero, the inverse filtering was the perfect uh choice.

**1:05:42** · But, again, what we have here is that we need to have uh information about the power spectrum of the noise and also of the power spectrum of the undegraded image, right?

**1:05:58** · So, to remedy these issues, we can use the definition for signal-to-noise ratio, which basically is a metric to measure the level of the original undegraded image power to the level of the noise power.

**1:06:14** · So, signal-to-noise ratio is defined uh as the double summation over all values of u and v of f hat u of u and v squared over the double summation over all values of u and v of uh n u and v.

**1:06:34** · So, f hat u and v uh in the frequency domain, if you remember from before, we said that there is a relationship between the uh the power of the signal in the frequency domain and the power of the signal in the uh signal domain. I'm not going to get into that um that much.

**1:06:58** · But, basically, this is the representation of the signal-to-noise ratio in the frequency domain, and in the signal domain, we have this uh representation of the uh signal-to-noise ratio.

**1:07:12** · So, to simplify the Wiener filter based on the signal-to-noise ratio, first, we assume we have a white noise, which basically means that its uh spectrum is going to be a constant value. That's the first assumption.

**1:07:27** · The second assumption is that we assume that the ratio between the power spectrum of the undegraded image and the power spectrum of the noise image is constant, right? So, first, we assume that sn is a constant value, then second, we assume that the ratio sn over sf is constant.

**1:07:52** · So, that is one thing that uh probably not 100% accurate all the time, right?

**1:07:59** · But, to simplify this, uh the Wiener filtering, we make this assumption.

**1:08:06** · now, if we do these simplifying assumptions, the Wiener filtering is represented uh in this simpler equation.

**1:08:16** · f hat of u and v equals 1 over h of u and v, uh absolute value of h of u and v squared over absolute value of h of u and v squared plus k multiplied by g of u and v. Basically, the inverse filtering result multiplied by uh this term.

**1:08:36** · And here, k is a constant that is added to the term to all terms of uh absolute value of h of u and v uh squared. now, let's just see how uh it looks in practice.

**1:08:51** · So, on the left image, we have the result of uh inverse filtering without applying any uh filter to limit the uh values of the transfer function in the frequency domain. Basically, the this image is repeated.

**1:09:14** · The second image is the result of uh again, inverse filtering, but now we limit or we radially limit the um the transfer function for the degradation, right? So, as you can see, it is much better than this one, but it still it is a bit blurry.

**1:09:37** · And finally, for the last one, we have the result of uh Wiener filtering. So, just by modifying the equation for inverse filtering and make uh make it into a Wiener filtering, we can get a a better result for uh restoration of the image. And we um the Wiener filtering is more resilient against um having noise when you compare it to uh inverse filtering.

**1:10:09** · So, let's take a look uh at more examples to see how Wiener filtering can perform better when compared to simple inverse filtering. So, on the top left corner, we had 8-bit image of the book cover that is corrupted by motion blur as well as additive noise.

**1:10:30** · The second image on the top uh row is the result of applying inverse filtering. And as you can see, not much of the image details uh are recovered in the result.

**1:10:43** · On the top right corner, however, you see the result of Wiener filtering.

**1:10:47** · Even though the resulting image is a a bit noisy and it still contains some motion blur, it's much much better than the simple inverse filtering.

**1:10:58** · So, now let's see what happens if we reduce the amount of noise.

**1:11:02** · So, this image is uh basically up uh degraded by the exact same amount of motion blur, but the the noise variance is reduced one order of magnitude.

**1:11:18** · Again, when you simply apply inverse filtering, you don't see that much effect. Basically, inverse filtering is not uh able to recover the image, but now the result of Wiener filtering is much better than what it was before. And finally, if you almost completely uh eliminate the the noise. So, here, in comparison to the previous one, the variance of the noise is reduced by five orders of magnitude.

**1:11:52** · Now, you can see the effect of uh inverse filtering to some extent, even though uh you're able to see the features, but it's still uh it is not per- perfect. On the other hand, the Wiener filtering can uh reconstruct an image that is uh almost exactly similar to the uh original image.

### Constrained Least Squares Filtering

**1:12:20** · So, now let's take a look at another method, constrained least squares filtering. So, the Wiener filtering is capable of image restoration, but it requires uh the power spectrum of the undegraded image and also the noise to be known.

**1:12:36** · And these are the two things that we generally don't have access to.

**1:12:41** · So, this new method uh only requires the mean and variance of the noise to be known.

**1:12:48** · And to reduce the effects of noise, or basically to reduce the noise sensitivity of the restoration process, uh we can consider a measure of smoothness to be applied to the image.

**1:13:01** · Uh for example, by using a second derivative of the image or the Laplacian, we can measure if the image is uh uh less uh smooth or more smooth. So, as you remember, the Laplacian was uh used to sharpen the images, right? So, because of that, it can be used as a measure of a smoothness.

**1:13:22** · So, if um the Laplacian, or you can say the the summation of the Laplacian in an image is very large, that basically means that the image is not as smooth and uh probably it is noisy. Of course, if the Laplacian is a small, then it means that the image is uh a smoother.

**1:13:46** · So, in the frequency domain, the solution for this approach can be shown like this. So, F hat of U and V equals uh H star of U and V, the complex conjugate of H of U and V, divided by uh absolute value of H of U and V squared plus um this parameter gamma multiplied by P of U and V, basically the absolute value of P of U and V squared multiplied by G of U and V.

**1:14:18** · Of course, you are not going to be asked to derive this equation. If you are interested, you can go take a uh look at the corresponding section in the book. Uh in terms of implementation, the implementation is very similar to the implementation of the Wiener filtering in the frequency domain. But the way to derive it it's a bit more uh probably more or less involved.

**1:14:46** · As we said, the gamma is uh an adjustable parameter, and P of U and V is the Fourier transform of the uh function uh and that is shown here. P of X and Y is a 3 by 3 matrix that is basically the the Laplacian kernel, one of the Laplacian kernel that we had.

**1:15:13** · So, now let's see how this thing can be implemented in practice and how the results look like. So, the functions P of U and V and H of U and V must have the same size, and that is something that is understandable here because we have this arithmetic addition here, and we have this uh basically element-wise subtraction. So, they need to be exactly of the same size, otherwise this doesn't make any sense.

**1:15:44** · So, if H is M by N, then P of X and Y should be embedded in the center of an M by N arrays of zeros, right?

**1:15:54** · So, P of X and Y by itself is 3 by 3, right? So, if you want to create a Fourier transform uh with size M by N, that means that the P of X and Y should also be M by N. So, what you need to do is that you embed this or you zero pad this along all directions to make its size uh M by N.

**1:16:19** · So, to preserve the even symmetry of P of X and Y, M and N must be even integers. So, it means that if the given degraded image is not of even dimen- dimensions, then a row and or column must be removed before com- computing H. So, these are some implementation details of uh applying constrained least squares filtering for uh image restoration. So, now let's just see how it looks uh in practice.

**1:16:51** · The image on the left is the result of this method uh applied to the previous image, which was uh affected both by motion blur and uh additive noise.

**1:17:05** · This one is with the same motion blur artifact, but with uh one order of magnitude reduction in the variance of the noise.

**1:17:16** · And finally, this one is uh with the same amount of motion blur, but five order of magnitude reduction in the variance of noise in comparison to this one. So, if you take a look at these images here, you see that mhm with a little bit of

**1:17:36** · different assumptions, the the new method uh is performing uh even a little bit better than the Wiener filtering, even though the function for Wiener filtering was to have access to the spectrum of power spectrum of the undegraded image and the and the noise, which were not possible. So, considering this measure of a smoothness or Laplacian can help us uh in recovering the original image.

### Geometric Mean Filter

**1:18:09** · So, now let's take a look at the final approach that I want to uh introduce today, and it is uh a geometric mean filter.

**1:18:19** · Of course, it is a little bit different than the geometric mean filter that we saw in a spatial filtering, this geometric mean filter is uh applied in the uh frequency domain. So, the Wiener filter can be generalized in the form of a uh geometric mean filter as follows.

**1:18:36** · F hat of U and V equals uh H star U and V, uh power spectrum of H of U and V, uh this uh ratio is raised to the power alpha, and then multiplied by H star U and V, power spectrum uh uh of H plus beta S N of U and V, S F of U and V.

**1:19:03** · If you remember, S N was the power spectrum of the noise, and S F was the power spectrum of the undegraded image.

**1:19:12** · And this ratio is taken to the power 1 minus alpha, and then finally, these two are multiplied by G of U and V. So, in this formulation uh alpha and beta are non-negative real constant.

**1:19:29** · Um So, this, as you can see, is a generalized version of the Wiener filter.

**1:19:35** · So, when alpha is zero Sorry, when alpha is one basically, uh this term is going to be uh zero. Sorry, this term is going to be to the power zero, which equals one.

**1:19:49** · And this whole equation is reduced to the basic inverse filter.

**1:19:55** · When alpha is zero, the filter becomes what is known as a parametric Wiener filter.

**1:20:03** · Uh which reduces to a standard Wiener filter when beta is one.

**1:20:08** · And when alpha uh equals 1/2 and beta equals one the filter is called a spectrum equalization filter.

**1:20:18** · Uh The geometric mean filter is usually useful in image restoration since uh it represents a family of filters uh in a single expression. Of course, just like we did with Wiener filtering, it is usually very common to consider the the power spectrum of the noise to be a constant and also the power spectrum of the noise uh over power spectrum of the undegraded image to be uh also a constant, too.

**1:20:46** · So if we do that, then we end up with uh an equation with three parameters, alpha, beta, and K. So, changing these variables basically can give us uh different uh results.

**1:21:06** · So, by this, uh I'm going to finish up the topic of this chapter, image restoration. We saw several examples of image restoration techniques both in the spatial domain and in the frequency domain.

**1:21:22** · What comes next is fundamentals of image segmentation.

**1:21:26** · Uh different methods for point detection, line detection, edge detection, and then finally, I will go over techniques for uh image thresholding.

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Clippings Index#Digital Image Processing|Clippings Index - Digital Image Processing]] · [[Second Brain]] · **Map:** [[MOC]]
> **Prev:** [[05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 8 - Image Restoration In Spatial Domain|Digital Image Processing - Part 8 - Image Restoration In Spatial Domain]] · **Next:** [[05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 10 - Image Segmentation|Digital Image Processing - Part 10 - Image Segmentation]]
> **Related:** [[IPA]] · [[Probability & Statistics]] · [[AI & ML Roadmap]]
<!-- connections:end -->
