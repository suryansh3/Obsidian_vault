---
title: "Digital Image Processing - Part 7 - Image Filtering in Frequency Domain"
source: "https://www.youtube.com/watch?v=nnq1aYl-OgQ&list=PL2mBI0yFsKk-p73KQ4iPdsi10hQC4Zd-0&index=7"
author:
  - "[[ASIP-Lab]]"
published: 2020-07-13
created: 2026-08-12
description: "Topics:00:40 Review of the Previous Lecture16:55 Basics of Filtering in the Frequency Domain31:18 Image Smoothing Using Lowpass Frequency Domain Filters53:02 Image Sharpening Using Highpass Freque"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=nnq1aYl-OgQ)

Topics:  
00:40 Review of the Previous Lecture  
16:55 Basics of Filtering in the Frequency Domain  
31:18 Image Smoothing Using Lowpass Frequency Domain Filters  
53:02 Image Sharpening Using Highpass Frequency Domain Filters  
1:07:57 Selective Filtering  
1:13:37 The Fast Fourier Transform (FFT)

## Transcript

**0:01** · Hello guys, welcome to the seventh lecture of the ENG860 uh special topics digital image processing course.

**0:10** · So, today I want to continue the discussion of chapter four with image filtering in the frequency domain. So, the topics that I'm going to cover in this lecture are the basics of filtering in the frequency domain.

**0:25** · Then on image smoothing using low-pass frequency domain filters. Then image sharpening using high-pass frequency domain filters.

**0:34** · Then selective filtering and then finally the fast Fourier transform.

### Review of the Previous Lecture

**0:40** · So, like before, before I start the new topics, let's just go briefly over what we discussed last time.

**0:47** · So, the first thing that I I want to cover is about the concept of 2D sampling and 2D sampling theorem.

**0:54** · If you remember, we said that if we have a function f of two variables t and z, we say that the the function is band-limited if its frequency components fall within a a specific range.

**1:10** · So, for that to happen, the horizontal frequency components should fall between negative u max and positive u max and the vertical frequency components should fall uh between negative v max and positive uh v max. So, in that sense, mathematically, the capital F of u and v, the Fourier transform of the original function is going to be zero when u and v are outside this range.

**1:42** · So, for such a function, the 2D sampling theorem states that a continuous band-limited function can be recovered without any error from a set of its samples that are captured using uh a 2D impulse train.

**2:00** · That happens only if the sampling rate over the two variables t and z follow these two constraints. So, 1 over delta t, basically the sampling rate in the t dimension should be larger than two times the u max and the sampling rate in the z direction, 1 over delta z, should be larger than two uh v max.

**2:24** · So, graphically, if you have uh this uh as the Fourier transform of the continuous domain, when we do 2D sampling, we are basically creating infinitely many uh replication of this uh Fourier transform at locations of the uh impulses in the impulse train.

**2:50** · So, when we do that, as long as this mm range is limited, what we have is basically uh no overlap between uh the two copies if these two conditions are satisfied.

**3:13** · So, this is the case when the two conditions are not satisfied.

**3:18** · Of course, it's possible that only one condition is satisfied and one other the other one is not satisfied. In that case, we only have overlap along uh only one direction.

**3:32** · So, the effect of not satisfying those two conditions is aliasing, which basically occurs when we do sampling or even when we do resampling of the images. So, here on the left we have the original image and there is no visible aliasing, but if we reduce the size of the this image uh to 1/3 in each dimension,

**3:59** · now we see these extra pattern that appear that were not there in the original image and that is the effect of aliasing. As before, if you do image smoothing before resampling, we can reduce the aliasing because image smoothing is basically applying a low-pass filter that suppresses the uh high frequency components.

**4:23** · So, that way it can reduce the amount of overlap between the high frequency components and reduces the effect of aliasing.

**4:33** · Then last time we went over a summary of all the DFT definitions. We talked about the the forward DFT, the inverse DFT for 2D images.

**4:45** · We had the definition for a Fourier spectrum, the phase angle, the polar representation of the Fourier transform, the power uh spectrum.

**4:55** · Um these were the basic definition that we had uh for the 2D discrete Fourier transform.

**5:04** · We also talked about the average value, which basically says that the average value of the image can be derived from uh the basically the zero frequency component of the Fourier transform as well. So, and if you follow these two equations, basically if you replace um the value for u and v uh in this equation as zero, then you get to this uh conclusion.

**5:38** · We also talked about the period periodicity of both the discrete Fourier transform and its inverse and how it can make some of the analysis a little bit more challenging, uh especially when we talk about convolution.

**5:55** · So, uh here, instead of having regular convolution, we have to uh perform circular convolution and to make sure that there is no error in the performance performance of the circular convolution, we had to uh have uh extra padding on the on the signals to avoid any overlap and error in the uh calculation of convolution.

**6:20** · The same can be said about correlation, too, but for most intention and purposes, we work with convolution because convolution in the frequency domain is equivalent to multiplication. Sorry, convolution in the signal domain is equivalent to multiplication in the frequency domain and we saw that convolution is basically the basis for uh spatial filtering in the images.

**6:48** · We also talked a little bit about the fact that the 2D DFT kernels are separable. So, that basically means that we can perform 2D DFT by mm two one-dimensional DFTs, one along the rows or columns and the other one along columns or rows.

**7:09** · And then finally, we saw that how we can obtain the inverse discrete Fourier transform using the algorithm that we had for the forward discrete Fourier transform. The only thing that we need to change is that if we pass the um complex conjugate of the Fourier transform to the uh algorithm for the forward discrete Fourier transform, we basically get a weighted version of the complex conjugate of the original image.

**7:43** · We also went over some of the DFT pairs. We didn't talk about the symmetry property that much.

**7:50** · You can refer to table 4.1 in the book.

**7:53** · But we talked about the linearity, the translation and also the rotation. We saw that the translation in the signal domain is basically uh changing the phase angle in the uh frequency domain. Also, if we translate the image in the frequency domain, it's basically equal equivalent to multiplying by this exponential complex function.

**8:22** · We saw that it is useful to translate or uh center the frequency rectangle.

**8:30** · And the way to do it is that in the frequency domain in the signal domain, if we multiply all the image pixels by this function, we basically center the frequency uh transform.

**8:45** · And this equation can be derived using the equation the general equation that we had for translation.

**8:53** · The only thing that we need to do is that we replace uh u0 and v0 by m/2 and n over two.

**9:01** · We saw that for rotation, if we rotate the image in the signal domain, uh its effect is going to be the same in the frequency domain, too.

**9:13** · So, it looks as if we rotated the frequency response the exact same amount.

**9:19** · Then we saw the convolution theorem, basically saying convolution in the uh signal domain is equivalent to multiplication in the frequency domain and vice versa.

**9:31** · The same is true for correlation, too, but here it is a bit more tricky because we need to keep in mind that uh correlation doesn't have some of the nice properties of the convolution. So, it's a bit more uh complicated. But overall, uh it is going to be much more

**9:54** · straightforward to do convolution uh or correlation uh basically any equivalent form in the frequency domain which is going to be trans done using multiplication or element-wise multiplication to be more precise.

**10:15** · We saw the um discrete unit impulse and how it's Fourier transform is going to be a constant value. And the inverse is going to be true, too. So, if you have a constant image in the signal domain that is basically an impulse function in the frequency domain.

**10:37** · Then we saw how we can have a 2D box function and how its Fourier transform is going to be multiplication of two sync functions. So, here we have a more general uh rectangle function in which we have A and B as the parameters.

**10:56** · Uh that basically show the amount of shift of this um box function.

**11:02** · And that, as you can see, doesn't change the shape, but it introduces changes to the phase angle of the uh frequency response.

**11:14** · These two uh DFT pairs are very interesting as well. We have the discrete Fourier transform of the sign function which, if you remember, the sign function could be uh shown as a weighted summation of two complex exponential function.

**11:32** · So, if we use that uh alternative representation that basically translate to having uh the Fourier transform of a sign function as two individual impulse function in the uh frequency domain.

**11:50** · Of course, there are more much a little bit more detail, especially when it comes to the uh correspondence between the frequency of the sign function in the signal domain and the the amount of shift that each one of these impulses have. But as you can see, it is pretty straightforward and you will see how these can be very useful in interpreting um the frequency transform of images, too.

**12:19** · Then we had the DFT pair for the cosine function, which is again is a similar uh concept as before because we saw before that cosine function can also be represented as a summation of two um complex exponential function. So, the Fourier transform of a cosine function is basically represented by a summation of two uh impulse function in the frequency domain.

**12:50** · And then finally, we have these two DFT pairs which are uh in general available for the continuous variables.

**13:02** · So, we have the differentiation which basically uh shows the relationship between differentiating the signal in the signal domain and its representation in the Fourier domain.

**13:15** · And vice versa.

**13:17** · Uh and also we have the uh fact that Gaussian functions in the signal domain are going to have a Gaussian shape in the frequency domain as well. So, these two are the thing that we see later on as well. Just to keep in mind that these equations are derived based on uh assumption of having functions with continuous variables. So, for the cases of discrete functions, we basically do sampling in either uh signal or uh frequency domains.

**13:52** · So, the next thing that we discussed last time was between the Fourier spectrum and Fourier phase angle, which one is more important. So, to show that, we used this uh example of this image and we calculated the discrete Fourier transform for this uh image. So, the second picture shows the the phase angle of the Fourier transform. As you can see, it looks very random.

**14:25** · So, uh now the question is uh which one of these two is more important, either the Fourier spectrum or the phase angle.

**14:36** · So, the third picture is the reconstruction of the original picture by but by only using the phase angle.

**14:43** · So, the Fourier spectrum is considered to be a constant. And then uh we used only the phase angle to do the reconstruction. So, even though all the in intensity informations are lost, but we still see uh the structure of the image is basically the very sharp edges. So, you see these sharp edges uh around the uh clothes of the boy and like around the its color are visible. You can see hint of the eye as well.

**15:12** · And even some of the dots that are appearing in the background, too.

**15:20** · But what if we do it the other way? What if we consider the phase angle to be constant and we only use the Fourier spectrum to do the reconstruction. So, if we do that, this is the image that we get. So, basically, there is no structure information in the reconstruction. So, based on these two reconstructions, we can uh conclude that phase information uh or phase angle contain more information of the image rather than the uh Fourier spectrum.

**15:53** · To show it further, this is the image of the boy reconstructed using uh its own phase angle information, but with the uh Fourier spectrum information of the the rectangle image that we had in the previous uh lecture. So, as you can see, we have a little bit of the intensity information.

**16:16** · But mostly, it is lost, but I still since we use we are using the phase angle information of the boy image, we can get a much better reconstruction even though the Fourier spectrum is from another image.

**16:31** · And this one is the rectangle image reconstructed using its own phase angle, but with the spectrum of the boy's image. Again, you see the vertical rectangle uh very good. Even though it's not 100% perfect.

**16:49** · But the shape information is mostly preserved.

### Basics of Filtering in the Frequency Domain

**16:56** · So, as for the basics of filtering in the frequency domain, which is going to be the topic of this uh lecture there are a few notes that you need to have in mind.

**17:07** · So, if you refer back to the equations that are used for performing forward discrete Fourier transform, you realize that the Fourier transform is computed by combining of the values of the signal in the spatial domain modified by the values of the exponential terms.

**17:27** · So, for uh calculating any of the Fourier transform components, we are basically using all the intensity values of the signal.

**17:41** · So, because of that, in general, it is impossible to make direct correspondence between uh between a specific components of an image and its Fourier transform because any uh frequency component is calculated by combination of all the uh signal components.

**18:01** · So, this is mainly because the frequency is uh related to the uh rate of change, not not necessarily the uh pixel values.

**18:15** · So, for example, if you have, let's say, five pixels that are all having the same intensity, let's say the intensity is five for all of these.

**18:25** · Since there is no change basically in the frequency domain uh you have a different representation.

**18:35** · uh As if you had, let's say, two of them having a uh value of three and the last three had a value of 10.

**18:45** · Right?

**18:46** · On the other hand, if you have five pixels with the same uh intensity uh even though you multiply the intensity values by a constant the frequency information is not going to change uh that much because at the end of the day, there is no variation in the uh intensities. Even though the amplitude amplitude got uh higher.

**19:14** · So, this is the main takeaway here that the frequency is related to the spatial rate of change and not necessarily the intensity values themselves.

**19:26** · So, based on that, we can associate frequencies in the frequent in the Fourier transform with patterns of intensity variations in the image.

**19:35** · So, if you want to do filtering in the Fourier domain what we basically do is that we modify the Fourier transform to achieve a specific objective.

**19:46** · And then we follow it up by inverse Fourier transform to uh get uh the spatial domain representation of the process result. So the general procedure looks something like this. We have the Fourier transform of the image.

**20:02** · We divide some um filter transfer function and we do element by multiplication. Then the next step to get the spatial domain representation of the filtered image, we perform inverse discrete Fourier transform.

**20:20** · And since the image that we started with is not a complex image, it's real image.

**20:27** · So it's only natural to take the real component of that image.

**20:34** · So now based on this, we can have a seven-step procedure for filtering an image in the frequency domain.

**20:43** · So the first step for filtering in the frequency domain is to have the input image f of xy with size m and n and we extend its size either by zero padding, mirror padding, or replicate padding to make sure there is not going to be any overlap in the frequency domain representation.

**21:06** · So we zero pad, mirror pad, or replicate pad this image and make a padded image of size p and q.

**21:16** · p by q in which p is 2m and q is 2n.

**21:21** · Then the next step is to multiply this padded um image by this function at any pixel location. And this is to center the Fourier transform.

**21:34** · Then the next step is to compute the discrete Fourier transform f of u and v of the padded image from the previous step, step two. Now in the frequency domain, we construct a real symmetric filter transfer function h of u and v of size p by q. So basically the size pq is the same size as f of u and v.

**22:05** · And this filter should be centered at location p over two and q over two.

**22:12** · Then we perform the element-wise product between h and f.

**22:19** · This is basically equivalent to doing a convolution in the signal domain.

**22:25** · Now that we have found the um filtered version of the image in the frequency domain, now what we do is that we calculate the inverse discrete Fourier transform of the image. Again as I said in the previous slide, since we have the original image to be a real-valued image we only take the real part of this

**22:51** · inverse discrete Fourier transform and to eliminate the effect of the initial multiplication by this function that we did to center the Fourier transform, we basically um multiply the result of step six by this function again at any pixel location.

**23:14** · And then finally, to obtain the final filtered result we basically extract g of xy of the same size as the input image by extracting the m by n region from top left corner of the gp of xy. So this is all words. Let's just see how it works in action.

**23:40** · So here on top left, we have this um electron microscope image that we want to do um Gaussian smoothing in the frequency domain. So the first step that we do is basically we pad the image.

**23:58** · Here we zero padded the image and unlike before when we did padding symmetrically along all dimensions of the image since in the frequency domain um the frequency response is only going to be calculated for this uh um this size, basically p by q.

**24:21** · As long as we are consistent with all of our all of the other steps, there is no need to do padding symmetrically in all directions.

**24:35** · So the next step is to multiply the padded image by the function -1 to the power x + y and we do it for all the individual pixels and for each individual pixel we have a coordinate x for the row and a coordinate y for the column.

**24:54** · And that's why some of the pixels are going to be multiplied by one, some of them are going to be multiplied by -1.

**25:00** · But the effect is that um the Fourier transform is going to be centered. Now we calculate the discrete Fourier transform. Here we see the uh spectrum of the Fourier transform. And as you can see, it is centered at the origin.

**25:20** · Then we have the centered Gaussian low-pass filter transfer function.

**25:26** · If you remember from the previous slide, we said that it's common to have a a filter transfer function that is real and symmetric around the origin.

**25:36** · So now the next step would be to multiply this function element-wise with the uh Fourier transform of the original image. So we multiply it by the Fourier transform, not only the Fourier spectrum but also the phase angle, too.

**25:52** · And this is the the result. So here we only show the the spectrum of the product. Now the next step is to calculate the inverse discrete Fourier transform of the image.

**26:07** · And then take the real part of it out and then multiply it again by -1 to the power x + y. And then finally, as you can see, the filtered image appears on the top left corner of the uh of this image. So what we do is basically we extract uh a rectangle of the same m by n and that is going to be the the filtered image.

**26:39** · So here let's just quickly take a look at some of these filters in the frequency domain. We will go over more detail later on, too. So here again we have the same uh electron microscope image.

**26:54** · If we have the transfer function for h to be a Gaussian we expect to have a smooth version of the image.

**27:04** · What if we work with a high-pass Gaussian filter? So the transfer function looks something like this. In that case, we basically eliminate all the low frequency component which in the spatial domain they are regions of constant uh intensity and what we end up with is basically all the edge information.

**27:32** · And then finally, for the last one we have again a Gaussian high-pass filter, but this time we have a shift or basically a translation of the uh frequency component at the origin. So they are not completely removed as they did here. But they are a little bit uh reduced.

**27:56** · So in that case, not only we have the intensity information of the constant intensity region, but in addition to that we have uh a much sharper representation of the image because applying this filter um sharpens the image. You will see later on how we can design these type of filters.

**28:23** · So in general, there are two ways to do um filters. We can either specify the filter in the spatial domain or we can specify the filter in the frequency domain. As for the implementation uh if you specify the filter in the spatial domain, what we need to do next is to do a spatial convolution to get the filtered result.

**28:45** · On the other hand, if we specify the filter in the frequency domain, we can use dft and idft to perform filtering in the frequency domain. Here you will see more example of this.

**29:00** · Um on the bottom left corner, you see uh a smoothing 1D Gaussian smoothing filter.

**29:13** · And on top of it, you see its Fourier domain representation. Of course, these are continuous functions. In reality, what we do is that we do sampling either in the spatial domain or in the frequency domain. Here you see two representative kernels that are sampled from this Gaussian function.

**29:33** · On the other hand uh here we see a version of a Gaussian high-pass uh image and its spatial representation looks something like this. Of course, if we do filtering, we see that and if you pay attention to these kernels, you see that this is equivalent to performing Laplacian in the signal domain.

**30:00** · And this is another introductory example to show that um filtering in the frequency domain and filtering in the spatial domain, if you consider all the conditions correctly, they produce identical result. So, on this image, we have the original image of the house and this is the Fourier spectrum of this image. Of course, it is centered.

**30:26** · On this side, we have a spatial kernel uh that is used to do edge detection and this is the uh perspective representation of it in the frequency domain.

**30:41** · Here is basically the same transfer function shown as an image. So, any uh value that you see here is shown with a darker value. Any peak that you see here is shown with a brighter value.

**30:55** · And these two are basically result of filtering in the frequency domain and result of filtering in the uh spatial domain. And as you can see, they are all uh identical.

**31:10** · So, now that we saw this, let's just see how we can create filters for smoothing and sharpening.

### Image Smoothing Using Lowpass Frequency Domain Filters

**31:18** · So, edges and sharp intensity transitions, such as noise, contribute to high frequency components in the frequency domain.

**31:26** · So, in effect, smoothing or blurring can be achieved by high frequency attenuation or low pass filtering. So, here we talk about three different types of filters.

**31:39** · Low pass filters, we have the ideal low pass filter. We have the Gaussian low pass filter and finally we have the Butterworth low pass filter, which is a filter that can act in some cases close to an ideal low pass filter and in some cases close to a Gaussian low pass filter.

**32:00** · Butterworth filters are controlled by a parameter called the filter order and large values of the filter order result in shape similar to the ideal low pass filter.

**32:13** · While if we use a smaller values, we have a shape that is similar to a Gaussian low pass filter.

**32:21** · So, the ideal low pass filter is a filter that passes without attenuation all the all of the frequencies within a circle with a specified radius from the origin and cuts off all the frequencies outside the circle.

**32:37** · So, if you want to show it mathematically, we can represent it in this form. H of U and V is one if D of U and V is less than D0 or if it's going to be zero if D of U and V is going to be greater than D0. As you can see, we have two unknowns here that we haven't defined before.

**33:01** · One is D0, which is the cutoff frequency, and then we have this function D of U and V, which for the ideal low pass filter is defined in this form. So, if you look closely, you see this is representative of a circle equation centered at P over two and Q over two, basically the origin of the uh frequency domain for the centered uh frequency response.

**33:28** · So, this is the perspective view of an ideal low pass filter. As you can see, whenever the frequency is in this range, the amplitude of it is going to be one.

**33:41** · That basically means that the filter passes all the frequencies in this range without any attenuation. But if you have a frequency that is outside this range, it's going to be multiplied by by zero.

**33:53** · Basically, it's going to be completely uh suppressed.

**33:58** · This is a top view version of this uh filter. As you can see, whatever is inside the circle is going to be with a value uh one here shown as a white and any region outside is showing uh with a value zero zero or uh black. And this is a one-dimensional profile of uh this image. Of course, it's shown from the the center of the frequency domain um to the right.

**34:30** · And as you can see, D0 is the cutoff frequency, which basically shows that how uh any frequency uh less than or greater than mhm this D0 is going to be affected. So, now the question becomes that how we can select the cutoff frequency. And that has to do with the specific application.

**34:58** · So, one way is to specify the percentage of the image power that you want the filter to pass.

**35:05** · So, to calculate the total image power, what we need to do is that we basically sum up all the Fourier spectrum components squared.

**35:17** · So, P P is subscript T is basically the summation of all the uh Fourier spectrum components squared.

**35:29** · So, now as for the percentage, uh it's going to be 100 times the summation of all the uh P's that fall inside the the circle inside the circle with the cutoff frequency D D0.

**35:46** · So, let's say we have this original image and we if we calculate its centered Fourier transform, this is uh the general shape that it can have. You see some circles that are shown here. To be exact, five circles.

**36:02** · And these circles are basically showing some sample uh D0 cutoff frequencies. So, we have the smallest one with D0 being 10. Then we have the next one with D0 being 30.

**36:16** · Then uh 60, then 160, and then 460.

**36:23** · And if we calculate this uh percentage, when the uh D0 is 10%, we are basically passing 87% of the image power.

**36:35** · For D0 of 30, we are passing 93.

**36:39** · For 60, we are passing 96. For 160, we are passing 98. And for 460, we are passing uh 99%.

**36:49** · One thing that you might notice is that uh even when we are using a D0 of a very small, we are still passing a lot of the uh image power. And the reason for that is usually the Fourier transform is very concentrated around the origin.

**37:12** · So, this image by itself is shown using a log transformation to basically be able to show the wide range of the uh frequency components values.

**37:27** · So, now let's see how these five different um D0s affect the the image.

**37:34** · So, here on top left, we have the original image, which is of the 5688 by 688.

**37:41** · And the following five images are basically the result of applying ideal low pass filter with different D0s.

**37:49** · So, here is the result of the ideal low pass filter with D0 equal 10.

**37:56** · This one is with D0 equal 30.

**37:59** · D0 equal 60. D0 equal 160. And D0 equal 460. So, the first thing that you notice is that there is not much difference between D0 being 160 and D0 being 460.

**38:13** · And if you refer to the percentages that we had, going from D0 160 to 460 basically does not change the amount of power that the filter uh passes.

**38:26** · But the uh effect is more dramatic for D0 being 10, D0 being 30, and D0 being uh 60.

**38:37** · Another thing that you might notice is that because of the the filtering, we see some ringing artifacts in the result of the uh applying the filter.

**38:49** · And that is basically one of the main issues with the ideal low pass filter.

**38:55** · So, to see the spatial representation, we can calculate the inverse discrete Fourier transform of the ideal low pass filter.

**39:04** · So, here on the left, uh we see the ideal low pass filter in the frequency domain. And this is the result of applying the inverse discrete Fourier transform. As you can see, uh we have uh basically ripple uh ripple effect.

**39:20** · If we look at the profile, we basically see we have a very like several points of zero crossing that contribute to the uh effect that we see when we apply ideal low pass filter mhm to the image.

**39:38** · So, if you remember from the Fourier transform of the box function, 2D box function, we saw that uh uh its Fourier transform is uh similar to uh it's basically a multiplication of two sync functions.

**39:59** · So now, if we have a similar shape in the frequency domain, its especially representation is uh basically similar with having zero crossing point. So, to be more accurate and we don't derive the equation here, the profile of the inverse discrete Fourier transform of the ideal low-pass filter is similar to a sync function.

**40:22** · In In to be more accurate, it's actually a Bessel function, which its derivation is out of the scope of uh this course.

**40:33** · One other thing that is known here is that we have the inverse proportionality between the width of the filter function in the frequency domain and the spread of the uh width of the lobes in the uh spatial domain.

**40:51** · So, basically, what happens is that when we uh increase the value of D0, in effect, we are uh decreasing the spread of the uh lobe of the spatial function in the spatial domain. So, when we have uh larger D0s, the spatial representation of the ideal low-pass filter looks more and more like an impulse function.

**41:21** · And that's why when we work with uh ideal low-pass filters with high values of D0, you don't see any effect because the convolution of any image uh with an impulse function is the image itself.

**41:39** · So now, let's see how we can basically eliminate these ringing artifacts. So, the next low-pass filter that we talk about is the Gaussian low-pass filter.

**41:50** · So, the transfer function of a Gaussian low-pass filter with cutoff frequency uh D0 can be shown using this exponential equation. So, H of U and V is E to the power negative D squared of U and V and two uh over 2 D0 squared.

**42:10** · As before, D the function D of U and V is basically defined in this form.

**42:18** · Basically, uh measures the distance between the origin of the frequency domain and any given point.

**42:28** · So, if we show the representation of this filter this Gaussian low-pass filter, the perspective looks something like this. As you can see, the transition from the zero frequencies to higher frequencies is much more smoother.

**42:47** · If we show it from a top top view, this is what we get. So, any uh bright region that we have, that means that uh it is going to have less attenuation, but in the dark region, we have the maximum attenuation.

**43:07** · And here, you see a 1D profile of uh this image drawn from the center of the frequency response going through in the right direction.

**43:19** · As you can see, by changing the values of D0, we basically have a Gaussian function with different spread or different width.

**43:30** · So, now let's see if the Gaussian low-pass filter performs better uh without any uh ringing artifact. So again, here we have the original image with size 688 by 688. And these are the result of applying five Gaussian low-pass filters with D0s being 10, 30, 60, 160, and 460.

**43:53** · One thing that you might notice is that in comparison to the ideal low-pass filter, we have less of smoothing when we are using the same D0s.

**44:09** · And the reason for that the transition is much much smoother in the Gaussian low-pass filter, but the upside is that we don't get any uh cross uh uh zero.

**44:31** · Basically, it doesn't have any points of crossing zero.

**44:36** · So, applying this filter, we basically uh don't get any ringing artifact.

**44:44** · And as you can see, since the Gaussian filter is isotropic in all the directions, uh the the smoothing happens uh much more uniformly across the image.

**44:58** · So, there is no distinction between vertical or horizontal or like diagonal edges.

**45:06** · So, the third type of low-pass filter that we want to talk about is the Butterworth low-pass filter. So, the transfer function for a Butterworth low-pass filter of order N with cutoff frequency D0 is shown in this form. So, H of U and V is 1 over 1 plus D of U and V over D0.

**45:31** · This fraction is going to be powered to two multiplied by N. Again, uh function D of U and V is basically to show distance between any given uh point in the frequency domain and uh the center.

**45:53** · So, this is the perspective representation of the Butterworth low-pass filter and this is uh a top view of that.

**46:03** · So, between the two, it is very like hard to see the effect of the uh filter order N.

**46:11** · But if we draw a profile view, we see that changing the value of the N basically changes the shape of the Butterworth filter. So, if we have higher values of N, as you can see here, we have much sharper transition between the uh lower frequencies and the higher frequencies.

**46:31** · But if you are working with uh smaller values of N, now you see that the transition happens much more smoothly.

**46:39** · So, that's why Butterworth filters uh can be designed in such a way to either resemble the behavior of ideal bypass low-pass filters or Gaussian low-pass filters.

**46:54** · So, now let's see what is the effect of Butterworth low-pass filter on the image that we had uh before. So, in this example, we use the same cutoff frequency as before. And as for the order of the filter, we use value N equals 2.25.

**47:16** · So, as you can see, the performance is almost similar to the Gaussian filter. But now, the question becomes uh whether we see any ringing artifact for different values of uh N.

**47:30** · And the answer to that is yes, it all depends on the value of the filter order, as we said.

**47:38** · If we use higher values of the filter order, the Butterworth low-pass filter looks more like an ideal low-pass filter, which had ringing artifact. On the other hand, if we use lower values of the filter order, the Butterworth low-pass filter looks more like a uh Gaussian low-pass filter.

**48:02** · So, as for the ringing, uh if we change the uh order N, we basically see uh effects of ringing artifact.

**48:14** · So here, in this image, we have spatial representations of the uh Butterworth low-pass filters.

**48:22** · So, here we designed the uh filter transfer function to be of size 1,000 by 1,000 and the cutoff frequency for all these four filters is going to be five.

**48:37** · But what we did was that we basically changed the uh the order. So, for the first one, with cutoff frequency of five, we have an order of one, which basically means that we have a wider spread uh in the frequency domain, which translate to a narrower spread in the uh spatial domain.

**49:01** · If we increase the filter order, for example, if we get to 20, that is equivalent to having a narrower spread in the frequency domain, which translate to a wider spread uh of the function in the spatial domain.

**49:17** · And and this is what you see here.

**49:21** · Basically, we end up having points of zero crossing, which translate to having ringing artifact. So, it is uh very important to uh modify the filter order in such a way so we can avoid the uh ringing artifacts.

**49:41** · So now let's see how these low pass filters can be used in applications.

**49:46** · So one of the applications that we see here is for text image processing.

**49:52** · Especially for processing images of a scanned document.

**49:59** · So by using a smoothing or blurring filters, we basically can a bridge a small gaps and repair the broken characters in the scanned document. So here on the left we see an example in which if you look closely we have these um uh gaps and broken characters.

**50:18** · By applying a low pass filter, even though we smooth the the image, but it still it is a still recognizable and as you can see if you if you zoom at the same section, there is not much gaps between the different parts of the character. So that can help a lot when we are using automated systems for character detection.

**50:47** · Another example is in printing and publishing industry uh which is used for cosmetic processing for a smoothing and creating uh images with a much softer look and also to reduce sharp sharpness of fine skin lines and small blemishes. So on on the left we see an image and if we zoom at the eye region, we see that there are some uh scan lines, sorry, skin lines that we have.

**51:19** · What happens is that if we apply um low pass filter, we basically can get get rid of those fine skin lines. Of course, as you can see these type of images uh a smooth the image uh as a whole.

**51:36** · In another word, they smooth it indiscriminately. So not only they uh uh smooth out these fine skin lines, but also they smooth out very sharp boundaries too. So to take care of that, um there are more specialized smoothing filters that uh do not affect all the regions the same amount. Of course, they are out of the scope of this uh course.

**52:07** · And finally for the last example, we can see an application of low pass filtering that is used to reduce machine induced artifacts. For example, in this image that is acquired using a very high resolution radiometer, you see that we have these scan lines that appear as the nature of the imaging process uh procedure for this VHRR device.

**52:36** · And if we apply a smoothing, we basically can reduce the effect of these horizontal scan lines.

**52:43** · Also, uh low pass is smoothing is uh a capable of a smoothing all the small features that are less than a certain size, which that certain size is decided by the value of the cut off frequency.

### Image Sharpening Using Highpass Frequency Domain Filters

**53:02** · So now that we saw uh image smoothing in the frequency domain, let us see how we can do image sharpening in the frequency domain.

**53:10** · So as before, edges and sharp intensity transitions, including noise, contribute to high frequency components in the frequency domain.

**53:20** · So image sharpening is used to basically sharpen the fine details of the images. And to do that, we can apply high pass filtering, which attenuate uh low frequency component without disturbing high frequency component.

**53:38** · So let's discuss some of these uh high frequency high pass uh frequency domain filters.

**53:48** · So here we see ideal high pass filter, Gaussian high pass filter, Butterworth high pass filter.

**53:53** · And then we talk about Laplacian and unsharp masking and high boost filtering in the frequency domain.

**54:01** · So this page is a summary of uh the three high pass filters uh that basically use the definitions that we had for the uh low pass filters. So if you if you remember from a previous lecture, we said that the transfer function of a high pass filter can be derived uh from a transfer function of a low pass filter.

**54:29** · So the transfer function of the high pass filter H of HP is basically 1 minus H of LP.

**54:38** · H of LP is the transfer function of the low pass uh filter.

**54:43** · So based on that, we can go directly from the ideal ideal Gaussian and Butterworth low pass filter and create the ideal Gaussian and Butterworth uh high pass filter.

**54:57** · For the ideal high pass filter, uh if the distance is below D0, the value of the filter is going to be zero. And if it's outside that, the value of the filter is going to be one.

**55:09** · And here you see a perspective view of the high pass filter.

**55:14** · Here you see a top view and also a profile, a side profile of the filter. As you can see, at location D0, any frequency that uh its distance is less than D0 is going to be attenuated completely.

**55:32** · But any frequency that uh its distance is greater than D0 is not going to be attenuated at all.

**55:41** · As for the Gaussian and Butterworth, the same situation happens. Of course, here the transition going to be much a smoother. So here you see a perspective view of the Gaussian high pass filter.

**55:53** · This is the top view and this is a a side profile view. And this one is the Butterworth high pass filter uh in perspective view, top view and side profile view.

**56:11** · So the spatial kernel can be derived by applying the inverse discrete Fourier transform to the uh uh high pass frequency response.

**56:22** · So if you want to see what is the spatial kernel for these type of high pass frequencies, we basically apply the inverse discrete Fourier transform to the transfer function of the uh high pass filter. So as you saw before, the transfer function of the high pass is 1 minus the transfer function of the low pass.

**56:44** · So now we have to calculate the inverse discrete Fourier transform of this constant function and this uh low pass function. So the discrete Fourier transform of a constant function in the frequency domain is going to be an impulse.

**57:02** · And this is basically the spatial uh representation of the uh low pass transfer function. So the spatial representation of the high pass filter is going to be a delta minus the spatial translation representation of a low pass filter.

**57:24** · So if we uh show it um in a spatial form, as you can see here, we have this additional impulse that basically is as the result of calculating the inverse discrete Fourier transform of a constant function.

**57:44** · So now let's see uh how these things perform in practice. So on on the top row, we have the same image as before, which is filtered by ideal high pass filter, Gaussian high pass filter, and Butterworth high pass filter using a cut off frequency D0 of 60.

**58:09** · So as you can see here, um these results are mainly uh showing the edges and boundary information and the regions of constant intensity are almost completely eliminated. And you know that those regions are correspond to low frequency components.

**58:30** · Another thing that you might see is that you are still see ringing artifacts in the result of ideal high pass filter.

**58:38** · And if I go back a little bit, you see that that is something to be expected we have because we have a locations of zero passing in the in its spatial representation uh as well.

**58:51** · The second row is basically uh the same sequence, but with a higher value for the cut off frequency.

**59:04** · So what are some of the examples of using a high pass filter? So one example is to enhance fingerprint images. So on the left you see a smudged uh thumb print.

**59:20** · In the middle, you see the result of high pass filtering.

**59:24** · And then finally, if we apply uh intensity thresholding and as we saw in the previous chapter, to the filter result, we see a much sharper representation of the thumb print.

**59:40** · So, now let's just see how we can perform more complex task task in the frequency domain.

**59:49** · So, if you remember from before, we could define the Laplacian operator in the spatial domain by summation of the second order derivatives along the horizontal and vertical directions and summing them up together. So, this is the Laplacian operator represented in the spatial domain.

**1:00:07** · If we use the differentiation property of the discrete Fourier transform, we can convert this equation from the spatial domain into the Fourier domain and get this equation. So, H of U and V for the Laplacian operator in the frequency domain is going to be equal to -4 pi squared multiplied by U squared plus V squared.

**1:00:40** · So, one thing that we need to do is that this operator by itself is okay, but since we centered the Fourier transform at the beginning for for our images, it's only natural to center the Laplacian operator as well, too. So, to do that, we basically shift the uh U and V frequency components to the center.

**1:01:06** · So, instead of U, we use U minus P over two, and instead of V, we use V minus Q over two. And if you do that, we see that this now resembles the distance function that we had before.

**1:01:21** · So, now everything is consistent. So, the Laplacian operator in the frequency domain in a centered frequency domain is going to be -4 pi squared D squared.

**1:01:37** · As for the convolution theorem, if we apply the uh element-wise multiplication between this transfer function and the Fourier transform of the image and we calculate its inverse, we basically get the Lapla- the result of Laplacian operator in the uh spatial domain.

**1:01:57** · So, now let's see how we can do image sharpening using this Laplacian operator in the frequency domain.

**1:02:05** · So, if you remember from before, the image sharpening using Laplacian operator in the spatial domain had an equation of this form. So, we basically add the original image with a uh with a weighted version of its Laplacian. So, the Laplacian is used to basically detect the edges and sharp transitions in the image.

**1:02:29** · So, if we choose the coefficient C properly, that basically means that this the result of this summation is basically the original image with additional information with regard to edges and sharp transitions.

**1:02:46** · So, in the frequency domain, if you want to represent this, we can just say G of X and Y equals the inverse discrete Fourier transform of the Fourier transform of the original image plus C H of U and V multiplied by F of U and V.

**1:03:05** · So, we saw that H of U and V is basically -4 pi squared D squared.

**1:03:12** · And for this purpose, if we chose the value of C to be -1, you remember before C could be positive or negative depending on the uh weights of the kernel that we were using for calculating the Laplacian operator.

**1:03:31** · So, if we do that, the image sharpening using Laplacian operator in the frequency domain looks something like this.

**1:03:39** · The inverse discrete Fourier transform of 1 + 4 pi squared D squared.

**1:03:47** · This all element-wise multiplied by the Fourier transform of the image.

**1:03:53** · So, to avoid any scaling in the images, it's recommended to normalize the original image to the range zero and one. So, if your image is eight bit, it value intensity values range from zero and 255.

**1:04:11** · So, what you need to do is that that you need to normalize it to the range zero and one, and also you need to normalize the Laplacian to the range -1 and one.

**1:04:24** · And if you do that, then everything uh is in order now. So, by just simply calculating this equation, you basically can get image sharpening using Laplacian operator.

**1:04:39** · Here you see a one example of it in uh action. So, we have this blurred image of the moon, and here we have a sharpened image of it uh of the moon by using the Laplacian operator in the frequency domain.

**1:04:56** · So, now let's see how unsharp masking and high boost filtering work in the frequency domain.

**1:05:02** · So, if you remember from before, for unsharp masking, what we did was that we created a mask from our image that was basically a subtraction of the original image and the a smooth version of it. So, this mask is basically uh similar to the original image, but it's only containing uh edge and sharp transition information of the image.

**1:05:32** · And then, the next thing that we needed to do was to add this uh mask uh to the original image with a weight K.

**1:05:44** · So, in the frequency domain, that is basically uh straightforward. So, the the first thing that we need to calculate is the low pass version uh image the low pass filter of the image, which is basically the inverse discrete Fourier transform of the multiplication of the low pass transfer function and the original image.

**1:06:10** · So, based on that, the mask is going to be the inverse discrete Fourier transform of the frequency transform of of the original image minus uh the multiplication of the transfer function of the low pass filter and the uh original image.

**1:06:30** · So, if we combine all these equations together, we see that the unsharp mask version of the image is the inverse discrete Fourier transform of 1 + K multiplied by 1 minus H of LP multiplied by F of U and V.

**1:06:48** · So, if we replace 1 minus H of LP with H of HP from a previous slide, we saw that the high pass filter is 1 minus uh the low pass filter in the frequency domain, then the equation is going to be simplified uh to this. And here you see uh an example in practice. So, here we have this uh blurry X-ray image.

**1:07:16** · This is the the mask that we create using this equation, and if we sum these two up with a proper value of K, this is a uh an unsharp mask version of the uh the original image.

**1:07:32** · And finally, if we do histogram equalization or histogram processing, we can get an image that contains much more information with regard to the in comparison to the original image, the final image is much sharper and it has a better ranges of intensity and contrast.

### Selective Filtering

**1:07:59** · This is a this table is something that I borrowed from a previous lecture, and that was basically showing the correspondence between a spatial kernel and frequency kernels.

**1:08:15** · So, we already saw the low pass kernels in the uh spatial and uh frequency domain. And also, we already saw the uh high pass kernels in the uh spatial and frequency domain.

**1:08:33** · What about What about band reject filter? So, as we saw before, band reject filters can be derived by a summation of a low pass kernel and a high pass kernel.

**1:08:45** · So, since this is basically a linear operator, its Fourier transform representation is going to be exactly the same. So, in the frequency domain, uh a band reject filter is basically the summation of a low pass filter and a high pass filter. Of course, these two can have different frequencies.

**1:09:08** · What about a band pass filter? A band pass filter in the frequency domain is 1 minus a band reject filter. And in the spatial domain, that is equivalent to subtracting the band reject spatial kernel from a uh delta function or an impulse function.

**1:09:28** · Here you see perspective plots of an ideal, a modified Gaussian, and a modified Butterworth uh filter of order one.

**1:09:38** · And all of these are band-reject filters. So, the reason that we use like the modified term here is basically if we just simply calculate these uh uh arithmetic operators, what we end up with is that uh we never get to uh to zero, right? In some of the cases, especially when we are working with uh Gaussian or Butterworth filter.

**1:10:03** · So, we need to do a small adjustment so we can get uh zero values when for the frequencies that we want to reject. Of course, you can refer to the book and see how these uh tiny tweaks can be performed, but the general idea is basically uh as it's described here.

**1:10:27** · Another type of selective filtering, which is very useful and which is something that I'm going to discuss in a little bit more detail for in the next chapter as well, is notch filters. So, notch filters can have two types. They are either notch reject filters or notch pass filters.

**1:10:49** · And they are uh designed to reject or pass uh frequencies in a predefined find a small neighborhood uh of uh in the uh image. So, notch reject filters are constructed usually by product of several high-pass filter transfer functions with the centers translated to the centers of the notch that we want to have. So, here you see an example of a notch reject filter. So, this is the general formulation of the notch reject filter.

**1:11:21** · As you can see, we have the product. This is the symbol that shows the product of its argument. And then we have h of k and h of um negative k.

**1:11:38** · So, if you remember at the beginning of the lecture, I talked about how if we have a sine function and cosine function, uh their Fourier transform representations are um impulse basically two impulse functions.

**1:11:53** · So, you see um the result of sine and cosine interference in an image is uh in this picture. As you can see, we have the original image, but we have this grid-like pattern that basically uh interferes with the original image.

**1:12:12** · If you calculate the Fourier transform, you see that we have these um impulses or like burst of energy that are basically symmetric with regard to the to the origin of the frequency response.

**1:12:27** · So, that is a behavior that is common uh for because of the sine and cosine interference, because those uh the frequency transform representation of a sine and cosine is basically two impulses that are symmetric with respect to the uh origin. So, now if you want to get rid of these using the previous filters, uh it's not going to be possible.

**1:12:59** · That's why we need to uh design notch filters to be able to remove uh a a smaller region of the frequency response. So, if we use uh basically uh eight notch filters to remove these uh impulses that we have, and then we reconstruct the image, we have an image that basically doesn't have any of those sine and cosine or like grid lock uh grid-like uh interference pattern in the reconstruction.

### The Fast Fourier Transform (FFT)

**1:13:38** · So, the last thing that I want to talk about in this lecture is with regard to fast Fourier transform. So, before I do that, let's just go quickly about over two uh nice properties of the 2D discrete Fourier transform.

**1:13:54** · The first thing was that the uh 2D discrete Fourier transform kernel, this complex exponential function, is separable. So, that means that instead of instead of performing the 2D discrete Fourier transform all at once, we can do it uh either by applying 1D discrete Fourier transform on rows and then on columns or vice versa.

**1:14:19** · So, in mathematical terms, this is the equivalent to separating the two components of the uh disc uh complex exponential function.

**1:14:33** · So, instead of having this, we uh separate it into a function that has only uh u and x as its variables, and another one that has v and y. And if we do that, we basically can separate between the two summations. First, perform um this summation, and then we use the result of this to perform the second one.

**1:14:57** · So, in effect, we are calculating the uh one-dimensional discrete Fourier transform, for example, for the columns first, and then we uh do it for the rows first or uh for the rows next, and vice versa. So, going from 2D kernel to 1D kernel significantly reduces the amount of calculation that we need to have.

**1:15:21** · And this is something that you saw before in the last chapter when we were talking about separable kernel in the spatial domain as well.

**1:15:32** · Another nice property that we had for the uh discrete Fourier transform is that we can basically use the same uh algorithm that we designed for um forward discrete Fourier transform to perform inverse discrete Fourier transform, too.

**1:15:50** · So, basically, if we pass the complex conjugate of the Fourier transform to this original summation that you see here, what we get is a scaled uh version of the complex conjugate of the the original function. So, these were two nice properties that helped us reduce the amount of calculation and software development for implementing um 2D discrete Fourier transforms.

**1:16:22** · So, now let's see how um the implementation of the discrete Fourier transform uh is performed, and what are the uh computational complexity of an implementation of a discrete Fourier transform.

**1:16:40** · So, a brute-force implementation of the discrete Fourier transform requires calculations on the order of m by n uh squared.

**1:16:52** · So, m is the number of rows, n is the number of columns. And to do a brute-force implementation of discrete Fourier transform, we basically require this amount of multiplications and additions. For the exponential terms, they are usually calculated once and stored as a lookup table. So, let's just see what it what it means for a regular-sized image.

**1:17:15** · So, if we have an image of 248 by 248, doing a brute-force implementation requires 17 trillion calculations, which is a very huge number.

**1:17:31** · So, the discovery of or the invention of fast Fourier transform basically reduced the amount of calculations several orders of a magnitude.

**1:17:42** · So, for fast Fourier transform, the amount of calculations is reduced to mn log two of mn multiplications and additions.

**1:17:54** · So, for an image of size 2048 by 2048, performing a fast Fourier transform algorithm requires only 92 million calculations, which is several times uh several orders of magnitude uh smaller than as if we did it uh as a brute-force implementation of the discrete Fourier transform.

**1:18:20** · So, to see the computational advantage, let's just assume that we have images of size m by m, and m being uh a power of two. So, two, four, uh eight, 16, 32, so on and so forth.

**1:18:37** · So, if we uh draw the computational advantage of the fast Fourier transform over brute-force implementation of the 1D discrete Fourier transform, this is the graph that we get. So, the computational advantage for value of p equals two to the power p uh over p. As you can see, as we uh an increased number of rows and columns, this computational advantage becomes more and more significant.

**1:19:09** · For example, if you're working with uh images of size two to 15 multiplied by two to 15, doing it using fast Fourier transform means that we can do the calculations almost 2,000 times faster than if we did a brute force implementation.

**1:19:28** · So, that's why um the invention of fast Fourier transform basically uh brought uh discrete Fourier transform or Fourier transform into mainstream, especially for signal and image processing application.

**1:19:46** · I'm not going to go over the details of how fast Fourier transform is uh derived. There are several versions of fast Fourier transform, and there are uh codes that are freely available uh online that you can use to perform fast Fourier transform.

**1:20:05** · Uh for the software that we are using here, we use uh MATLAB that has fast Fourier transform implemented in it. So, for 2D images the function that you can use is FFT2, which is uh used to do forward um two-dimensional fast Fourier transform, and for the inverse, we have IFFT2.

**1:20:32** · There's another useful function that is commonly used, and that function is basically to center the Fourier transform. If you remember, to center the Fourier transform, we had to calculate um or multiply all the individual pixels with the function -1 to the power x + y.

**1:20:54** · But, the equivalent version in MATLAB is uh FFTshift and IFFTshift that basically uh FFTshift centers the Fourier transform, and uh IFFTshift basically uh brings back back the centered Fourier transform into uh its original location.

**1:21:19** · So, I highly suggest you go over the uh application of these uh four functions that I described, and go and read the um the MATLAB manual on how they can be used.

**1:21:35** · So, by this, I'm going to conclude the discussion of uh this chapter. In the next chapter, uh I'm going to talk about image degradation and restoration process.

**1:21:47** · Uh two types of degradation is going to be discussed. We have degradation as a result of noise, and we have degradation as a result of uh additional uh functions like uh blurring or um motion artifact.

**1:22:05** · I'm going to talk about noise models, and noise reductions using different types of filters, and then I'm going to introduce different ways to estimate the degradation function, and how we can use these estimates to basically eliminate the effect of noise or other type of artifacts that are common in the images.

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Clippings Index#Digital Image Processing|Clippings Index - Digital Image Processing]] · [[Second Brain]] · **Map:** [[MOC]]
> **Prev:** [[05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 6 - Discrete Fourier Transform (DFT)|Digital Image Processing - Part 6 - Discrete Fourier Transform (DFT)]] · **Next:** [[05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 8 - Image Restoration In Spatial Domain|Digital Image Processing - Part 8 - Image Restoration In Spatial Domain]]
> **Related:** [[IPA]] · [[Probability & Statistics]] · [[AI & ML Roadmap]]
<!-- connections:end -->
