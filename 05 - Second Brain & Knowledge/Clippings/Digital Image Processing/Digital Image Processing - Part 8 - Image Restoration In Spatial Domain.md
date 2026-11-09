---
title: "Digital Image Processing - Part 8 - Image Restoration In Spatial Domain"
source: "https://www.youtube.com/watch?v=oLkSslD9wcE&list=PL2mBI0yFsKk-p73KQ4iPdsi10hQC4Zd-0&index=8"
author:
  - "[[ASIP-Lab]]"
published: 2020-07-20
created: 2026-08-12
description: "Topics:1:04 What We Learned So Far ...4:14 Image Degradation/Restoration Model8:36 Noise Models32:55 Noise Parameter Estimation37:55 Restoration for Noise-Only Degradation – Spatial Filtering40:"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=oLkSslD9wcE)

Topics:  
1:04 What We Learned So Far ...  
4:14 Image Degradation/Restoration Model  
8:36 Noise Models  
32:55 Noise Parameter Estimation  
37:55 Restoration for Noise-Only Degradation – Spatial Filtering  
40:20 Spatial Filtering: Mean Filters  
48:20 Spatial Filtering: Order-Statistic Filters  
59:10 Adaptive Filters

## Transcript

**0:00** · Hello guys, welcome to the eighth lecture of the digital image processing course.

**0:05** · In today's lecture, I'm going to talk about image restoration in the spatial domain.

**0:11** · So, these are the topics that I'm going to cover in today's lecture.

**0:16** · I will talk briefly about image degradation and restoration model.

**0:20** · Then, I will introduce some of the common noise models in image processing applications.

**0:26** · Then, noise parameter estimation.

**0:30** · Then, restoration for images that are only degraded by noise.

**0:35** · Uh and you will see how we can use a spatial filtering to get rid of the noise.

**0:40** · Then, I will introduce three different types of spatial filtering.

**0:47** · Namely, we have mean filters, we have order statistic filters, and then finally, we have adaptive filters.

**0:53** · So, you have seen examples of these type of spatial filters before.

**0:58** · But, in today's lecture, I'm going to go over them in much more uh detail.

### What We Learned So Far ...

**1:05** · So, let's just quickly see what we have learned so far in this course.

**1:10** · So, we started with image acquisition.

**1:13** · Basically, how we can convert a continuous scene into a digital image. We said that to do that, we need to do sampling and quantization.

**1:24** · Then, we moved to intensity transformations.

**1:28** · We saw inversion, log transform, gamma correction.

**1:33** · Then, to more advanced one, which use histograms of the images.

**1:38** · So, we saw histogram equalization and histogram matching.

**1:43** · Then, we moved to spatial filtering. At the beginning, we started the topic using correlation, but then we extended that, and we introduced convolution, and we just concluded that convolution and spatial filtering are basically uh equivalent. And convolution has some nice properties that the correlation doesn't have.

**2:10** · So, it's usually recommended to do convolution when we do a spatial filtering as opposed to correlation because of the nice properties of the convolution.

**2:21** · Then, we saw some smoothing spatial filters, more specifically, box filter, Gaussian filter, and median filters.

**2:29** · Then, we saw some uh sharpening spatial filters, namely, Laplacian, gradient, and unsharp masking.

**2:37** · And then, in the last uh chapter that we discussed, chapter four, we talked about Fourier series and Fourier transform.

**2:49** · Uh mainly in continuous domain first, then we talked about how sampling would change uh Fourier transform, and what are some of the artifacts of sampling. We specifically talked about aliasing.

**3:07** · Then, we moved forward with the discrete Fourier transform, in which both the input signal and the output transform are discrete functions.

**3:17** · Then, based on the definition of discrete Fourier transform, we saw how low-pass filters and high-pass filters work. Low-pass filters are equivalent to smoothing filters in the spatial domain.

**3:28** · So, we saw ideal Gaussian and Butterworth low-pass filters.

**3:33** · And high-pass filters are generally equivalent to sharpening a spatial filter. So, we saw ideal, Gaussian, Butterworth, Laplacian, unsharp masking using uh discrete Fourier transform.

**3:47** · Then, we talked about selective filtering.

**3:51** · We went over uh band pass and band reject, and also, we talked about notch filters.

**3:57** · And finally, we concluded uh last chapter with a brief introduction on fast Fourier transform.

**4:05** · Uh and how it revolutionized the application of discrete Fourier transform in digital signal processing applications.

### Image Degradation/Restoration Model

**4:16** · So, let's just start talking about image degradation and restoration.

**4:21** · So, to do that, we should have a way to model uh image degradation and also restoration.

**4:30** · So, image degradation is a is modeled as an operator H together with an additive noise term.

**4:38** · So, if we have this original image that we want to capture, right? So, this can be considered as the true transformation from a continuous domain into a discrete domain.

**4:49** · But, because of all the uh properties of the camera and the scene and the weather, even, we may end up with a degraded version of this image. So, we have this degradation operator H that is applied to the image.

**5:05** · And also, we can have this additive noise term, too, N of X and Y.

**5:12** · Which these two combined create the image G of X and Y, which is the degraded image that we are capturing from the true image F of X and Y.

**5:25** · So, now, the restoration process says that if you have some knowledge about H, the degradation operator, and also some knowledge about the additive noise, is it possible to reconstruct the original image or not?

**5:46** · So, using the in this figure, you see both the degradation and the restoration. So, at the beginning, we talked about the degradation, and then later on, we talked about how we can restore uh images that are degraded.

**6:02** · So, this is something that we will show later, but uh if the operator H is linear and position invariant, then the degraded image is given in the spatial domain by this equation, G of X and Y equals convolution of H of H of X and Y and F of X and Y plus N of X and Y. So, N is the additive noise term.

**6:28** · F of X and Y is the original image that we want to capture, and H of X and Y is basically the impulse response of the degradation operator.

**6:39** · So, for uh operator H, if it is linear and position invariant, this is very important.

**6:48** · If these two conditions are satisfied, then the degradation is modeled with a convolution operator.

**6:57** · So, now, uh if we have this equation in the spatial domain, it's uh only natural to write the equation in the frequency domain, too. So, the capital G of U and V, basically, the Fourier transform of G of X and Y equals uh H of U and V multiplied by F of U and V plus N of U and V. Each one of these uh terms are the Fourier transform of the corresponding uh uh terms in the spatial domain.

**7:32** · And also, here, we use the convolution theorem, which uh specified that convolution in the spatial domain is equivalent to multiplication in the frequency domain, and vice versa.

**7:44** · So, now, let's just only focus uh on a case that is image degradation only with noise.

**7:52** · So, in this sense, in the frequency domain, you can say uh H of U and V is a constant function of value one.

**8:03** · So, in this case, G is going to be F of U and V plus N of U and V. In the spatial domain, this can be considered as when H of X and Y is an impulse at the center.

**8:18** · So, you remember that an impulse in the spatial domain was equivalent to a uh constant function in the frequency domain.

**8:27** · So, convolution of an impulse with uh any function basically gives the the original function itself.

### Noise Models

**8:38** · So, now, we need to model different types of noises.

**8:45** · So, usually, there are different uh sources of noise in digital images, but they generally arise during image acquisition or transmission. For example, in CCD cameras, uh the levels of light and also the temperature of the sensor are major factors in the amount of noise that you get in the uh in the images.

**9:05** · You have seen example of these uh before, too, that for example, if you're using your phone camera to capture an image in the low in low light, you realize that uh the amount of noise in the image is much higher as opposed to if you wanted to capture the same scene in uh uh much more brighter environment.

**9:32** · The same uh thing can happen during the transmission, too.

**9:37** · Which basically uh has the effect of interference in the transmission channel, you may end up having additive noise to your images, too. So, for example, in wireless transmission, uh lightnings or other atmospheric disturbances cause noise.

**9:54** · So, in a noise only degradation model, we have the original image f of x and y, which is in the degradation process, there is this noise term that is added to it, and then we end up having g of x and y. So, now the restoration process is tries to is trying to estimate the original image given some information about the noise.

**10:21** · So, what are those information that we can have about the noise?

**10:25** · What are some spatial and frequency properties of the noise?

**10:30** · One question that we we need to ask is that is the noise correlated with the image or not?

**10:37** · That's an important question. Uh so, for now mostly we we only work with noise that is uncorrelated with the image.

**10:50** · So, when the noise when the Fourier spectrum of the noise is is constant, the noise is called white noise.

**10:58** · The reason for that is because the physical property uh of the white light in which uh it contains all frequencies in the visible spectrum in equal proportions.

**11:10** · So, a white noise is basically uh represented as a constant function in the Fourier spectrum.

**11:22** · Why? Because it contains all the uh frequency components of the spatial domain.

**11:31** · With the exception of a spatially periodic noise, here we assume that the noise is independent of spatial coordinates.

**11:40** · And also we assume that it's uncorrelated with respect to the image itself. So, these are some simplification assumptions, because when you don't have these assumptions, the analysis of the noise is going to be much more uh complex, which is out of the scope of the course.

**12:01** · So, now based on this, let's just talk about some of the properties of of the noise.

**12:07** · So, we can model the statistical behavior of uh intensity values in the noise component of the image of the degraded image by a probability distribution function or a PDF.

**12:21** · So, this noise component is going to be an image with the exact same size as the input image.

**12:27** · Remember, if I go back, as you can see here, we we need to add f of x and y plus n of x and y to create g of x and y. So, this is an example of an arithmetical operation.

**12:42** · So, to for this to be valid, these two functions need to be uh exactly the same size. This is what we saw in previous chapters.

**12:57** · So, now what we do is that we can simulate noise images by generating arrays in which uh the PDF is some specified probability distribution functions that are well known.

**13:12** · So, there are some uh very important noise PDFs. We have the Gaussian noise, you probably have seen this before or have heard about it before.

**13:22** · We can have the Rayleigh noise, the Erlang or gamma noise, we can have the exponential noise, the uniform noise, and finally the salt and pepper noise.

**13:32** · So, out of these six, the first five, from Gaussian to uniform noise, they are applied to the image exactly similarly.

**13:40** · You can create a noise component, and then uh you add it to your original image. The salt and pepper noise is applied a little bit differently, which will which I will go over it in a later slide.

**13:55** · So, each one of these uh PDFs can be modeled based on two variables. So, we can have the mean value of the PDF, or we can have the and we can have the variance.

**14:07** · So, mean value usually shown with a bar, so z bar is the mean value of uh random variable z, which is also called the expectation of this random variable is defined as the integral from negative infinity to positive infinity of z multiplied by pz over dz.

**14:31** · So, z is the random variable itself, pz is its probability density function, or probability distribution function.

**14:41** · And if you take this integral, you get the mean value of this random variable.

**14:48** · Of course, in the discrete case, this is going to be reduced to a summation of z multiplied by its discrete probabilities.

**14:59** · As for the variance, which is commonly shown with sigma squared or v of z, we have the integral of z minus z bar, z bar calculated from the previous equation, squared multiplied by pz, and the integral is calculated over variable z.

**15:18** · Of course, for the discrete uh variables, uh you replace this with a summation, and also these z uh and pz are going to be discrete values.

**15:32** · So, now let's see how we can model these important noise PDFs in practice.

**15:41** · So, the first one is the Gaussian noise, which is the most frequency used PDF or noise PDF because of its mathematical tractability in both the spatial and frequency domain. If you remember from before, we said that the Gaussian function in the spatial domain is going to be equivalent to a function a Gaussian function in the frequency domain, too.

**16:06** · So, because of this, uh Gaussian noise is usually more common about uh in all the noise PDFs. Of course, Gaussian function has other nice properties, too. More specifically, Gaussian PDF, which we don't talk about them in this course.

**16:28** · Uh you can refer to relevant courses on probability to learn about the Gaussian uh PDF.

**16:38** · So, the PDF of a Gaussian noise is given by this equation: p of z equals 1 over uh square root of 2 pi multiplied by sigma e to the negative z minus z z bar squared over 2 sigma squared. And this function spans from negative infinity to positive infinity.

**16:59** · So, in this equation, z is representing the intensity.

**17:04** · Z bar is the mean or average value of z, and and sigma is the standard deviation of z.

**17:11** · So, a graphical representation of the Gaussian PDF is on the right. You have seen this before. It's a it's a bell curve.

**17:23** · Of course, one thing that you should note here is that this function that we described here are mainly continuous in the discrete domain, you take samples of these uh continuous functions.

**17:38** · The next uh noise PDF that we will see here is the Rayleigh noise.

**17:44** · So, the PDF of a Rayleigh noise is shown by this equation.

**17:50** · So, p of z equals 0 for z uh less than constant a, and for z greater than or equal constant a, it's going to be 2 over b z minus a e to the negative z minus a squared over b.

**18:11** · Now, you can see that we have two additional variables. We have a, and we have b.

**18:17** · But, by knowing the mean and variance, you can derive the values for a and b using these equations.

**18:25** · So, z bar equals a plus square root of pi b over 4, and sigma squared is b multiplied by 4 minus pi over 4.

**18:37** · So, if you know the mean and variance, you can plug it in these two equations and get the values for a and b. As for the graphical representation, this is the Rayleigh noise PDF. As you can see, uh it is right is skewed uh when you compare it to the uh Gaussian noise PDF.

**19:06** · Then we can have the Erlang or gamma noise.

**19:09** · So, the PDF for Erlang noise is given by this equation.

**19:14** · Uh p of z is 0 for z less than 0, and it's a to the power b z to the power b minus 1 over b minus 1 factorial multiplied by e to the negative az.

**19:30** · You see that the equation is very complex, but uh again, you can estimate the values of b and a just by knowing the uh mean and variance of the uh the noise PDF. You should also note that uh this equation is only valid for value of A being greater than B and B being a positive integer.

**19:59** · In this form, the Erlang this is called the Erlang noise, but B minus 1 uh factorial uh can be valid for uh values of B that are not uh integer, too. So, if you use that if you uh this definition for the factorial, which is the definition of gamma function, then you can have you can call this a gamma noise, as well.

**20:31** · And as for the graphical representation, you have this figure to the right that shows the graph of the uh Erlang or gamma noise.

**20:43** · Then the next one is the exponential noise. The PDF for the exponential noise is given by uh this equation, P of Z equals 0 for Z greater than 0, and it is A e to the negative AZ for Z greater Sorry, the next the previous one was for Z less than 0, and A e to the negative AZ for Z greater than or equal to 0. And in this equation, A is uh a positive value.

**21:15** · A cannot be negative, otherwise this function uh is going to be infinitely increasing, which makes the the area under the curve to be infinite, which is not possible for a uh PDF.

**21:34** · And in this equation, the mean and the variance of the variable Z are shown using these two equations. The the mean is going to be 1 over A, and the variance is 1 over A squared.

**21:47** · If you look closely, you realize that this is the special case of the Erlang PDF.

**21:53** · Uh the only difference here is that uh in the Erlang PDF, if you set B to be 1, then it reduces to the uh exponential noise.

**22:07** · The next one is the uniform noise.

**22:10** · So, the PDF for the uniform noise is given by this equation, P of Z is 0 when Z is outside the range A and B.

**22:21** · If Z is in the range A and B, the value is going to be 1 over B minus A.

**22:29** · And this is the graphical representation of uh the uniform noise.

**22:36** · Uh for the mean and variance of the uniform noise PDF, the mean is going to be A plus B over 2, and the variance is B minus A squared over 12.

**22:51** · As I said, the PDF for salt and pepper noise is a bit different. So, the PP the PDF of salt and pepper noise is given by uh this function. So, P of Z equals P underscore S for intensity values equal to 2 to the K minus 1. So, if you remember, K was the number of bits that you used to represent the intensity values.

**23:13** · So, for values of intensity being equal to 2 to the K minus 1 or the maximum possible intensity, we have the probability of uh salt noise to be P of S.

**23:33** · For values of intensity being 0, the probability of pepper noise, which is going to be P of P, and finally for Z being V, which is any value any other value outside of uh 0 and uh so, any other value uh than 0 or 2K minus 1, the probability is going to be 1 minus PS plus uh PP.

**24:02** · So, this is the graphical representation of the salt and pepper noise.

**24:14** · So, how we can apply such noise to the image? So, the way to do it is that given an image f of x and y of the same size as n of x and y, we would assign 0 to all locations in the image where 0 occurs in uh the noise component based on this probability.

**24:40** · The next is we assign a value of 2K minus 1 to all locations in the image where the value 2K minus 1 occurs uh in n.

**24:50** · And finally, we leave unchanged all locations in f of x and y where v occurs in uh in the noise image. So, you see the application of salt and pepper noise is a bit different than how you applied the previous types of noise. The previous ones, you created the noise component and you just added to uh to your image.

**25:12** · But now, in the salt and pepper noise, depending on the value of the uh noise at any given pixel, you either change the value of the original image to 0 or 2K minus 1, or you leave it unchanged.

**25:33** · So, salt and pepper noise is has uh other names, too. Sometimes it's called bipolar impulse uh or even unipolar impulse if either P of S or P of P 0. It's also called data drop dropout noise or uh a spike noise. So, the noise density P is defined as the probability of any pixel being corrupted by either salt or pepper noise.

**26:00** · So, P equals P of S plus P of P. For example, if you have an image in which P of S is uh 2% or 0.02, and P of P is 1% or 0.01, then the the noise density is going to be 3%. Which basically means that 2% of the pixels are corrupted by salt noise, and 1% is corrupted by pepper noise, and in total, 3% of the pixels are corrupted by salt and pepper noise.

**26:34** · So, the mean and variance of the uh salt and pepper noise as are defined uh in these two equations.

**26:45** · Uh So, Z bar is going to be 0 multiplied by uh P of pepper. So, we include 0 here to show that uh it it uh still uh basically contributes to the mean value, even though uh the 0 multiplication by P and P P of P is going to be 0, but it's still uh I included that, so you know that uh this is the the general equation.

**27:18** · Then we have V multiplied by its probability, then we have 2K minus 1 multiplied by its probability.

**27:25** · As for the variance, we basically can use the equation for the mean, and then we replace it in the equation for the variance that we saw before. And if we do that, this is the equation that we get for the variance of the salt and pepper noise.

**27:43** · So, now let let's take a look at some examples here. So, here on top left, we have this original image in which we have three different regions, each having one single uh intensity value. So, if I draw the histogram of this image, this is what it looks like in general. So, we have three peaks at the location of the three intensity values.

**28:10** · When we add the Gaussian noise, you realize that each one of these peaks that we had in the original image now is transformed into a Gaussian uh function. And the reason for that is that the the Gaussian PDF is actually showing a probability distribution function. So, not one single uh intensity value, but a range of intensity values. So, when you add it to the original image, then you have uh this shape for the image degraded by the Gaussian noise.

**28:45** · You can apply the same concept for the Rayleigh noise and Erlang noise. And as you can see, at location of each one of these peaks, you have uh these functions that look like the Rayleigh function or the uh Erlang function. Of course, you can change the parameters of each one of these uh noise PDFs, and then you may end up with uh functions that are either wider or narrower than what is shown here.

**29:20** · You can apply the same thing for the exponential noise. So, this is the original image degraded by the exponential noise. And as you can see, at the location of each one of these spikes, we have an exponential function now.

**29:35** · This one is for applying the the uniform noise.

**29:39** · Again, at location of each one of these the spikes, we have uh a uniform uh PDF.

**29:47** · And finally, for the salt and pepper noise, for the salt and pepper noise, it's a little bit trickier to see, especially since we had um this image in which it had uh an area that was uh completely uh black. So, when you apply it, you may end up with like extra uh uh spikes.

**30:11** · So, this uh example is not a very good example to represent the salt and pepper noise. Of course, this is this is the image that was chosen by the uh authors of the book. So, salt and pepper noise it's going to be more visible in terms of the histogram if you have an image uh in which you have all the like most of the intensity values that are possible for in that image.

**30:41** · In that case, you'll see uh distinguishable spikes at locations of zero and uh 2k minus 1 when you apply the uh noise salt and pepper noise to your image.

**31:01** · So, now let's see what happens with the periodic noise.

**31:04** · So, we have seen this example several times before. So, periodic noise in images usually arises from electrical or electromechanical interference during image acquisition.

**31:18** · Periodic noise is a specially dependent noise as opposed to the other types of noise that we disc- that I described in previous slides.

**31:30** · But, as you saw before, it can be reduced significantly in the frequency domain by applying frequency domain filtering, more specifically notch filtering.

**31:42** · Here is an example of an image that is affected created by a periodic noise.

**31:47** · And if you calculate the Fourier transform of this image, you realize that there are two sharp spikes that appear in the uh Fourier transform.

**32:00** · So, these two spikes are equivalent of this period periodic noise in the uh in the spatial domain. So, if you apply such a uh notch filter, basically anywhere is uh white, that means that uh any frequency component that fall in the white region are going to pass.

**32:23** · And we only have two dots with black value or zero value, which basically uh stop the uh the two uh spikes that are caused by the periodic noise. So, if you apply this mask to this image and then calculate the inverse Fourier transform, this is the image that we get. Uh you can see the periodic noise is completely eliminated uh in the in the result.

### Noise Parameter Estimation

**32:57** · So, now the question becomes, okay, we have an image that is that is noisy. How can we estimate the uh parameters of the of the noise?

**33:09** · So, for the periodic noise, parameters can be estimated by inspection of the Fourier spectrum because they usually produce frequency spikes in the Fourier domain.

**33:21** · But, for the for the other types of noise, the PDFs uh noise parameters can be known for from sensor specifications or estimated from the image acquired from the systems as well. So, if you have access to the imaging system that we use for capturing the image, what we can do is that we can capture a set of flat images, for example, by imaging a solid gray board with uniform illumination, and

**33:50** · then uh since we we already know what the image should look like, uh we can estimate the uh the amount of noise or the parameters of the noise uh from those flat images.

**34:06** · But, what if we only have the the images that are captured?

**34:10** · We don't have access to the imaging system.

**34:13** · So, in this case, what we can do is that we can estimate the PDF of the basically the noise parameters of the PDF from small patches of uh regions in the image that are mostly constant intensity.

**34:30** · So, this is an example of um this this procedure. So, let's say we have an image that has some regions with very with constant intensity. So, if you select those regions, and then we use the we basically draw the histogram uh of those regions, we can see that since the noise is applied uh to all the sections of the image uniformly, this is a good representation

**35:03** · of the uh amount of noise that is present to the to the image.

**35:12** · Uh so, this one is when the image is affected by a Gaussian noise. So, the histogram of the intensities in that small patch uh uh resemble a Gaussian PDF. This one is for a Rayleigh noise, and this one is for uh a uniform noise.

**35:34** · So, now uh let's say we created that, how we can estimate the mean and and the variance.

**35:43** · So, to do that, let's just consider the the image and S, and let's just assume PS of ZI for I changing from 0 to L - for I changing from 0 to L minus 1 is the probability estimates or the normalized histogram values for the intensities uh of the pixels in the patch, and L is the number of possible intensities. So, for an an 8-bit image, uh L is going to be 256.

**36:12** · So, now based on this, the mean and variance of pixels can be uh calculated based on the equation that we have for the mean and intensity as we saw before.

**36:23** · So, the mean is going to be the summation over I uh changing from 0 to L minus 1, ZI, basically the intensity value multiplied by its uh probability.

**36:35** · The variance is summation of ZI minus Z bar squared multiplied by the probability of intensity ZI.

**36:47** · Uh if the shape of the histogram is Gaussian, then mean and variance are uh on are the two parameters that you need. For other cases, except salt and pepper, if we know mean and variance, you can calculate parameters A and B for those type of noises.

**37:05** · For salt and pepper, you can calculate the actual probability of salt and pepper noise by counting them in uh in the in the patch and then dividing the total numbers by the and dividing the total number of each occurrence by the total number of pixels in the strip.

**37:26** · So, let's say you are working in a strip or like a in an image patch in which you have a thousand uh total number of pixels, and out of those thousand, 50 of them are uh affected by salt noise. So, in that case, the probability of salt noise is going to be 50 uh over a thousand, or it's going to be 5%.

### Restoration for Noise-Only Degradation – Spatial Filtering

**37:56** · So, now let's just see how we can restore images that are degraded by uh by noise. So, in this case, we only consider images that are degraded only by noise. So, we don't include any other type of degradation.

**38:13** · So, when the image is only degraded by additive noise, we have these two equations in the spatial and uh frequency domain. So, G of X = F of X and Y + N of X and Y.

**38:28** · And G of U and V = F of U and V + N of uh U and V.

**38:34** · So, if you know the noise component exactly, you basically can uh subtract it from the degraded image.

**38:43** · But, in reality, what happens is that you don't know the noise component. You may know some properties of the noise, but you don't necessarily know the the noise component itself.

**38:55** · For periodic noise, you probably can estimate the uh noise component in the frequency domain from the spectrum of uh the degraded image.

**39:06** · But, in in general, you don't know the noise component, only some noise parameters.

**39:15** · So, the way to estimate the original image from its degraded version is usually called denoising.

**39:23** · Uh And this is done in the spatial domain by spatial filtering.

**39:30** · So, we have seen some spatial filters before. So, in this lecture, we will go over more of these type of spatial filtering.

**39:40** · So, this is a summary of all the filters that we will cover here.

**39:43** · We have the mean filters including arithmetic mean filter, geometric mean filter, harmonic mean filter, and contraharmonic mean filter.

**39:53** · We will see order statistic filters which include median filters, mean max filter, midpoint filter, uh and alpha trimmed mean filter. And finally, we have adaptive filters uh including adaptive local noise reduction filter and adaptive uh median filter.

**40:15** · So, let's just go over uh the mean filters.

### Spatial Filtering: Mean Filters

**40:20** · So, just like what we discussed before is that when we are doing filtering in the images, we basically consider an a small neighborhood uh around pixel x and y in which pixel x and y is at the center.

**40:39** · So, we want to calculate the new value for the center pixel based on the intensities of its uh neighbor pixels.

**40:48** · So, at the arithmetic mean filter is basically the equivalent to the box filter that we we have seen before. So, in which the new pixel the new pixel value for location x and y is the average of uh the pixels in the degraded image in that neighborhood.

**41:08** · So, this is the mathematical equation for the arithmetic mean filter.

**41:12** · So, it's a very basic filter.

**41:15** · It is able to uh smooth uh local variations and also, it can uh reduce the noise, too.

**41:23** · But, a little bit more advanced uh mean filter is the geometric mean filter in which to calculate the new value for the center pixel, you first calculate the multiplication of all the pixels uh in the neighborhood and then you take it to the power 1 over mn. Basically, mn uh is the the size of the neighborhood.

**41:48** · So, if you are working in a 3 by 3 neighborhood, you calculate the word product of nine intensity values and then you take it to the power 1 over 9.

**42:00** · So, as opposed to arithmetic mean filter, geometric mean filter loses less image detail while the performance in terms of noise reduction is uh very similar to arithmetic mean filter.

**42:12** · Then, we can have the harmonic mean filter which works better for uh for only salt noise. So, in which the new pixel value for the uh center pixel is calculated by this equation mn over the average of the inverse of the intensity values.

**42:37** · And then finally, we can have the contraharmonic mean filter in which uh the new value for the center pixel is uh the average of the intensity values to the power q + 1 divided by the average of intensity values to the power q.

**42:58** · So, q is the order of the filter. If q is positive, this filter is more suitable for eliminating pepper noise. And if q is negative, it eliminates salt noise.

**43:12** · So, if q is zero, in that case, uh the contraharmonic mean filter is is reduced to arithmetic mean filter.

**43:22** · And if q is negative one, uh the contraharmonic mean filter reduces to the harmonic mean filter.

**43:31** · Of course, uh application of these uh filters on the images are very straightforward. What you need to do is that you need to uh scan the image row by row and column by column. For any given uh pixel, you define the rectangular neighborhood around it and then based on the intensity values, you calculate the new intensity value for that center pixel and then you replace it in the in the image.

**44:01** · Of course, you cannot do that uh on the on the image that you have. You basically need to create uh a new version of the image and do the calculations on that new version.

**44:17** · Uh So, let's just see how they perform for four images.

**44:23** · So, here we have an 8-bit uh x-ray image on the top left corner.

**44:31** · And then on the top right corner, we added a Gaussian noise of zero mean and the variance of uh 400.

**44:40** · Uh on the bottom left, you see the result of filtering with an arithmetic mean filter of size uh 3 by 3. And on the bottom right, you see the result of filtering with a geometric mean filter uh of size 3 by 3. When you compare these two together, the performance is mostly mostly similar. The only difference that you may see is in terms of the the edges.

**45:06** · So, as you can see, as you can uh compare uh as much as it's visible here. So, you can refer to your own slides and zoom in to see better. But, the sh- edges are much sharper in the result of imaging with uh filtering with the geometric mean filter uh as opposed to the uh arithmetic mean filter.

**45:39** · What about if you have either salt or pepper noise?

**45:43** · Uh image on top left is uh the image that we saw previously, but this time instead of being corrupted by Gaussian noise, it is corrupted by pepper noise with the probability of uh 0.1.

**46:02** · And on top right, we have the original noise-free image that is corrupted by uh salt noise with a probability of 0.1.

**46:13** · So, on the bottom left, you see the result of filtering uh this image with the contraharmonic filter with q being 1.5. And this one is the result of filtering uh the salt pep- salt noise degraded image with a contraharmonic filter with q being negative 1.5.

**46:37** · Uh if you remember from the previous uh f- uh previous slide, we said that uh a contraharmonic filter with positive q is uh more suitable for eliminating pepper noise.

**46:54** · And a contraharmonic filter with negative uh q is suitable for eliminating uh salt noise. So, you see the effects uh here.

**47:06** · So, in general, arithmetic and geometric mean filters are useful for random noise like Gaussian or uniform noise.

**47:13** · And the contraharmonic filter is useful for impulse noise, whether it's salt pepper salt noise, pepper noise.

**47:21** · Uh but, it must be known whether the noise is uh dark or light or whether you are dealing with pepper noise or uh salt noise.

**47:31** · And that is necessary for you uh because you need to decide on the sign of the uh the filter order or the q. Otherwise, the result that you get is definitely worse than the the initial image.

**47:47** · So, here in these two images, you see the result of selecting the wrong sign uh sign in the contraharmonic filter.

**47:55** · So, this is the result of filtering uh this image but with a negative value for q.

**48:03** · And this one is the result of filtering this image with a positive value for q.

**48:08** · As you can see, the result of filtering is definitely worse than the original uh image. So, you should uh keep that in mind if you want to use contraharmonic uh filters.

### Spatial Filtering: Order-Statistic Filters

**48:21** · Now, let's see how order statistic filters work.

**48:26** · So, in the mean filters, uh what you did was that you decided on a neighborhood around a center pixel and then you did some calculations uh on those intensity values. So, those calculations that we did before, the order of the intensity values didn't matter, right?

**48:44** · But, in order statistic filters, the order does matter because order statistic filters are the type of special filters whose response is based on the ordering or ranking of the intensity values in the neighborhood.

**49:02** · Uh So, you have seen the example of a median filter before.

**49:07** · So, to calculate the median filter, what you need to do is that you decide on the size of the neighborhood. You get the intensity values in that neighborhood and then you rank them or order them from uh smaller to larger or vice versa. Then, you took them you take the median value of uh this ordered set.

**49:32** · So, the equation for the new intensity values at location x and Y is basically the median of all the intensity values inside the uh inside the neighborhood.

**49:45** · Median filter is most useful for impulse noise.

**49:50** · Then we can have the max and min filters, which are defined using these two equations. Again, to get the max value, max intensity value in a set of uh pixels, you need to to order it. The same is true if you want to get the min intensity intensity value. So, max filter is usually good for removing pepper noise, and min min filter is usually good for removing salt noise.

**50:18** · Then you can have the midpoint filter, which is usually good for removing Gaussian or uniform noise, in which you calculate uh the average between the max intensity value and min intensity value inside the the neighborhood.

**50:36** · And finally, we have the alpha trimmed mean filter, in which you delete uh a portion of the intensity values inside the the region before you calculate the average. So, you delete D over two highest and D over two lowest intensity values in the neighborhood, then you take the average of the remaining pixels.

**50:58** · So, this is the equation.

**51:00** · Uh F hat X and Y, basically the new intensity value at location X and Y equals 1 over MN, the total number of uh pixels in the neighborhood minus D, and then sum of G uh R of ST. GR basically signifies that a portion of the intensity values are removed.

**51:25** · So, if D is zero in this equation, basically you don't remove any intensity values from the neighborhood, the alpha trimmed mean filter is equivalent to the arithmetic mean filter.

**51:39** · If D equals MN minus one, the alpha trimmed mean filter is equivalent to the median filter.

**51:48** · Of course, you can have uh values for D anywhere from zero to MN minus one, so then the performance is going to be somewhere between the arithmetic mean filter and the median filter. So, now let's take a look at some examples. Here on top left, we have the 8-bit X-ray image that is corrupted by salt and pepper noise, and the probabilities of corruption uh are uh 0.1.

**52:20** · So, you have equal port uh salt or pepper noise uh in this image.

**52:28** · So, on top right corner, you see the result of one pass with a median filter of size uh 3 by 3. So, even though the the amount of salt and pepper noise is highly reduced, there are still some pixels in the image that are the remnants of salt and pepper noise. So, for example, you see some pixels uh you you see some pixels here.

**52:55** · One thing that you can do is that you can apply median filter again.

**53:00** · And when you do that, you basically eliminate some of the remaining salt and pepper uh noise pixels. So, this is the result of applying median filter a second time.

**53:13** · And you see that there are still some minor pixels that are affected by salt and pepper noise.

**53:20** · So, one thing that you do is that you apply the median filter one more time, and that helps to uh reduce the amount of salt and pepper noise uh even further. Of course, you cannot do this uh indefinitely, depending on the on the image.

**53:39** · Uh you may need to do it more or less.

**53:42** · One thing that you need to keep in mind is that uh mm Application of uh median filter on the image uh basically uh smooths as the image too, maybe not as uh drastic as uh mean filters, which basically uh smooths out the the boundaries, but uh still you cannot apply a mean filter excessively because it removes some of the fine details of the of the image.

**54:19** · So, let's just see another example.

**54:22** · On top left corner, we have the 8-bit X-ray image, uh which is uh degraded by by pepper noise with probability of 0.1, and on top right, we have the same image uh corrupted by salt noise with probably 0.1.

**54:45** · And on bottom on the bottom uh on the left, we see the result of filtering with a max filter of size 3 by 3, and the result of filtering with a mean filter of uh size 3 by 3.

**55:01** · So, as you can see, they are good in eliminating either salt or pepper noise, but but not both, but not both, and also they ended up uh smoothing or narrowing some of the boundaries or the sharp edges of the image too. So, usually median filter is more preferred uh as opposed to max and min filter.

**55:27** · For some applications, you can apply mean and max filter, but generally speaking, a median filter is more preferred for removing salt and pepper noise.

**55:39** · Let's just take a look at another example. Here we have uh basically a a combined noise. So, on top left corner, we have the X-ray uh image with additive uniform noise of zero mean and variance of 800.

**56:00** · Uh Top um top middle, we added salt and pepper noise with probabilities 0.1 for both salt and pepper to the uh previous image. So, this image not only contains uh uniform noise, but also salt and pepper noise.

**56:20** · On top right corner, you see the the result of applying the arithmetic mean filter uh to the image. So, as you can see, the image is much better than the previous one, but there are a lot of features that are smoothed out and are not uh visible. So, in general, the arithmetic mean filter is not a good choice for getting rid of the combination of uh uniform noise and salt and pepper noise.

**56:52** · On the bottom left, you see the result of geometric mean filter, which uh as you can see, because you have uh pepper noise, the image is much darker. If you remember in the equation for the geometric mean filter, you have to calculate the the multiplications of the pixels or the intensities inside the neighborhood.

**57:16** · So, in any neighborhood that you have uh a pepper noise, since the intensity is zero, that means that the the multiplication becomes zero. So, generally speaking, geometric mean filter produces a a darker image. And of course, and also the performance is not uh that great either.

**57:39** · In the bottom center, you see the result of uh median filter.

**57:45** · As you can see, the image is much sharper when you compare it to the arithmetic mean filter, and it was able to uh get rid of get rid of the noise, of course.

**57:57** · The result is still very a little bit uh smooth, but just keep in mind that we have applied both uh uniform noise with very high variance, and also uh salt and pepper noise.

**58:11** · So, uh basic median filter uh basically did what it it could do, and the result is uh very good for such simple uh formulation. And finally, we have the alpha trimmed mean filter with D being six.

**58:34** · So, in any 5 by 5 neighborhood, uh we remove the three lowest intensity values and three highest intensity values, and then we calculate the uh the mean. And when you compare it to the median filter and any of the other filters, you see that the alpha trimmed

**58:57** · mean filter is able to produce a much sharper result with uh less uh blurring of the edges or narrowing of the boundaries.

### Adaptive Filters

**59:11** · So, in all of the these images that we discussed, um the filters are applied to an image without consideration of how image characteristics vary from one pixel to to another. So, whether a pixel's in the uniform region or whether it's next to an edge or boundary.

**59:32** · So, in reality, changing the filter parameters in an adaptive and local manner can improve the performance of the filters.

**59:42** · Of course, this comes at a cost, which means that we have a filter with more complexity or more time-consuming to be applied to the image.

**59:55** · So, here I talk about two adaptive spatial filters.

**1:00:00** · Um the first one is the adaptive local noise reduction filter, and the next one is the adaptive median filter.

**1:00:09** · So, for the adaptive local noise reduction filter, we work based on these values. So, we have g of x and y, as you saw before, is the value of the noisy image at location x and y.

**1:00:23** · We have the variance of the noise, sigma n squared. We have the local average intensities of the pixels in the neighborhood around the center pixel.

**1:00:35** · We show it with z bar, f of xy, and then we have the local variance of the intensities of the pixel in the neighborhood s xy, which we show it at the sigma squared s xy.

**1:00:50** · So, for implementing this filter, what we need to do is that we need to first know what is the variance of the noise.

**1:01:00** · If you remember before, we said that if we find a large enough patch or a strip in the image which contain mostly uniform intensity values, we can estimate the variance from those pixels in that and that patch.

**1:01:19** · So, this is the first step that we need to do.

**1:01:22** · Then for any neighborhood around the center pixel, we need to calculate the local average and local variance.

**1:01:31** · So, the behavior of the filter is intended to be like this.

**1:01:38** · If noise variance is zero, so basically if you don't have any noise in that neighborhood, then f of xy should be equal to g of xy. So, that is a trivial solution. If you don't have any noise, you don't have to do anything.

**1:01:53** · If local variance is high relative to noise variance, basically if you are near the edges, this is most common and in location near the edge that you have local variance that is higher than the noise variance, the filter should return a value close to g of xy.

**1:02:20** · And if the two variances are equal, basically the local area has the same property as the overall image, then you should perform averaging to reduce the noise.

**1:02:32** · So, let's just see what happen if you put all these requirements into an equation. So, f bar f hat x and y equals g of x and y minus sigma n squared over sigma s xy squared multiplied by g of x and y minus z bar s of x and y.

**1:02:57** · So, if the noise variance is zero, which basically mean that sigma n squared is zero, this equation returns f hat of x and y equals g of x and y.

**1:03:09** · If the local variance is high relative to noise variance, so that basically mean that sigma s x and y squared is larger than sigma n squared, so in this case, this ratio is going to be small, which makes this this term to be a small.

**1:03:32** · So, f hat x and y is g of x and y minus some very small value, which you can approximate it as g of x and y. And finally, if the two variances are equal, basically sigma n squared over sigma s xy squared is equal, so this ratio is one. In that case, this equation will simplify to f hat x and y equals z bar s x and y because we have g x and y minus g x and y, which which cancel out.

**1:04:07** · Of course, you can see that this filter is very simplistic, but even with its simplicity, it can perform very good. So, let's just take a look at one example. On top left image, we have an image that is corrupted by additive Gaussian noise of zero mean and a very large variance.

**1:04:30** · The variance is 1,000.

**1:04:32** · On top right corner, you see the result of arithmetic mean filtering.

**1:04:37** · So, even though it was able to smooth out most of the noise, but it also is smooth out a lot of the features of the image.

**1:04:47** · So, it is not a a good filter. On the bottom left corner, you see the result of geometric mean filtering.

**1:04:57** · So, as you can see, in uniform areas, the performance is usually the same with the arithmetic mean filtering. In regions near the edges, it can preserve edges better, but since the image that we have here is containing a a lot of noise, and since the filter that we use here is 7 by 7, it is still not ideal, and you see some thickening of the the boundaries and

**1:05:29** · regions, too, which basically, for example, if you look here, when you compare to the original image, you see that these edges are thickened to the point that you barely can distinguish them.

**1:05:43** · And finally, on the bottom right corner, you see the result of adaptive noise reduction filtering using the equation that we provided before.

**1:05:55** · Now, you see that using this adaptive noise reduction filtering, you can get much better result as opposed to just simple arithmetic mean filtering or geometric mean filtering. Not only it was able to get rid of the noise so much, but also it was able to preserve the edges, the sharpness of the edges very good.

**1:06:18** · And overall, it is a better substitute for arithmetic mean filtering or geometric mean filtering.

**1:06:28** · So, the next adaptive filter that I want to talk about here is the adaptive median filter.

**1:06:34** · So, the adaptive median filter can handle higher probabilities of salt and pepper noise in addition to a smoothing non-impulse noise.

**1:06:42** · So, the method works based on the following notation.

**1:06:46** · We have z min, which is the minimum intensity value in the neighborhood s xy.

**1:06:52** · We have z med, which is the median intensity value in the neighborhood s xy.

**1:06:57** · We have s max, which is the maximum allowed size for the neighborhood s xy.

**1:07:03** · We have z max, which is the maximum intensity value in the neighborhood s xy. And finally, we have z xy, which is the intensity at location xy.

**1:07:15** · So, just from these set of parameters, you see that we have s max, the maximum allowed size for s xy. So, we can conclude that one of the thing that we work with to make the median filter better is changing the the size of the neighborhood.

**1:07:37** · So, the adaptive median filtering contains two levels.

**1:07:41** · So, in level A, what we do is that we check the median value of the neighborhood to see if it falls between the the minimum value of the intensity or the maximum value of the intensity inside that neighborhood.

**1:07:57** · If this condition is satisfied, we go to level B, in which we check the intensity value at location x and y to see if it's between z min and z max.

**1:08:13** · If it's between z min and z max, that means that it is not going to be impulse like.

**1:08:20** · And in that case, we output z of xy for the for the value of the the pixel, so so it means that we don't change it.

**1:08:32** · If it's not between z min and z max, then we output the median value because from the previous state, we checked that the median value is not impulse like.

**1:08:44** · The other case is that the in the level one, that z min is either equal to sorry, z med is equal to z min or z max.

**1:08:54** · In that case, that means that the the median value is similar to an impulse.

**1:08:59** · So, in this case, we need to increase the size of the neighborhood.

**1:09:04** · So, we increase the size of the neighborhood as long as the size of the neighborhood is smaller than the maximum allowed size, then we repeat level A.

**1:09:16** · If we reach the maximum allowed size, we output the the median value as the output of the filter for the a center location.

**1:09:28** · So, the adaptive median filter algorithm has three objectives.

**1:09:32** · One is to remove salt and pepper or impulse noise.

**1:09:36** · Two is to provide a smoothing of other noise that may not be impulsive.

**1:09:41** · And three to reduce distortion such as such as thinning or thickening of object boundaries.

**1:09:49** · So, level A checks whether the median of the neighborhood is impulse-like.

**1:09:54** · If not, it goes to level B where it checks whether the center pixel is impulse-like.

**1:10:01** · If it's not, it returns the center pixel.

**1:10:05** · And if it if it is, it returns the median value.

**1:10:09** · If the median is impulse-like in the neighborhood uh when we check it in level A, then it increases the size of the neighborhood given the condition that the new size cannot be larger than the maximum allowed.

**1:10:24** · And repeats level A. If the new size is larger than the allowed size, it outputs the median.

**1:10:32** · So, note that the neighborhood size and the maximum allowed size are odd positive integers greater one greater than one. So, this is something that we have discussed uh before is that to have the center pixel truly at the center of the neighborhood, the size of the neighborhood should be uh odd in both dimensions. So, this is something that we have seen it before.

**1:10:56** · But, if you take closer look at the the logic behind the adaptive median filter, at any neighborhood, it checks whether the median is like an impulse noise.

**1:11:10** · Uh if it's not, then checks the center pixel. If it's not, that mean that the pixel is not affected by uh but by impulse noise. So, it returns returns the the value.

**1:11:22** · If it is, it assumes that okay, now that uh the pixel is affected by impulse noise and the median is not an impulse value whether zero or 255, then uh or basically the mean value or the maximum value inside the neighborhood.

**1:11:46** · Then it outputs that.

**1:11:49** · And then does a similar thing for uh for level A as well for the case uh when the the median is impulse-like, uh then it increases the size with the hope that the new median is not impulse-like. And then repeat this process for every pixel until it gets to the the final filtered result.

**1:12:13** · So, I highly suggest you go through the the steps of this algorithm and you try to uh rationalize it and you try to definitely understand it because as soon as you understand it, now now everything makes more more sense. So, now let's take a look at one example. So, here on the left we have the 8-bit X-ray image that is corrupted by high probability of salt and pepper noise.

**1:12:42** · So, we have 20% of 25% of the pixels affected by salt noise and 25% affected by by pepper noise. So, the original image is barely visible through the amount of noise that we have in this image.

**1:13:01** · In the at the center, we have the result of the filtering with a 7 by 7 median filter.

**1:13:07** · Even though the result was able to get rid of a lot of the the noise or most of the noise, but it is very blurry.

**1:13:19** · So, applying median filtering by itself is not enough to get rid of this amount of noise in this image.

**1:13:26** · And finally to the right, you see that this is the result of adaptive median filtering with Smax being uh being seven. Basically, the maximum allowed size for the neighborhood being seven.

**1:13:41** · So, when you compare these two results, one with the result of median filtering and one with the result of adaptive median filtering, it is clear that the adaptive mean median filtering is superior in comparison to the median filter.

**1:13:57** · There are a lot of features that you cannot even see in the in the noisy image, but the adaptive median filtering was able to recover. Like these tiny dots that you have in your uh circuit board.

**1:14:11** · If you look if you go and look at the original noise-free image, you see that they are visible in the original image, but in this noisy version, they are not visible. So, adaptive median filtering was able to recover uh most of the details of the image while eliminating mm basically all of the uh salt and pepper noise that degraded the image.

**1:14:38** · So, in today's lecture, I went over uh image restoration using a spatial filtering. In the next lecture, I will talk about periodic noise reduction using frequency domain filtering.

**1:14:54** · Then I talked a little bit little bit about linear position invariant degradation.

**1:14:59** · How to estimate the degradation function and then different uh methods to uh restore the image that is affected by uh linear position invariant degradation.

**1:15:14** · We will take a look at inverse filtering, minimum mean square error filtering or um well more well known as Wiener filtering, constrained least square filtering, and finally geometric mean filters.

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Clippings Index#Digital Image Processing|Clippings Index - Digital Image Processing]] · [[Second Brain]] · **Map:** [[MOC]]
> **Prev:** [[05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 7 - Image Filtering in Frequency Domain|Digital Image Processing - Part 7 - Image Filtering in Frequency Domain]] · **Next:** [[05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 9 - Image Restoration In Frequency Domain|Digital Image Processing - Part 9 - Image Restoration In Frequency Domain]]
> **Related:** [[IPA]] · [[Probability & Statistics]] · [[AI & ML Roadmap]]
<!-- connections:end -->
