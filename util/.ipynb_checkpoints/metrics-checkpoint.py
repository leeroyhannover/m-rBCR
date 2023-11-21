# metrcis
import tensorflow as tf
import numpy as np
from skimage.metrics import peak_signal_noise_ratio
from skimage.metrics import structural_similarity as ssim

def metrics(IMG1, IMG2):
    # input: pred, gt. return psnr, ssim, rmse
    
    # psnr
    psnr_value = peak_signal_noise_ratio(IMG1, IMG2,data_range=1)

    # ssim
    ssim_value = ssim(IMG1, IMG2, multichannel=True)
    
    # RMSE
    mse = np.mean((IMG1-IMG2)**2)
    rmse = np.sqrt(mse)
    
    return psnr_value, ssim_value, rmse

def metrics_func_mimo(y_true_list, y_pred_list):
    y_true, y_pred = y_true_list[0], y_pred_list[0]
    squared_difference = tf.square(y_true - y_pred)
    mse = tf.reduce_mean(squared_difference)

    # Define the maximum possible pixel value (1.0 for images in the range [0, 1])
    max_pixel_value = 1.0

    # Calculate the PSNR
    psnr = 10 * tf.math.log((max_pixel_value**2) / mse) / tf.math.log(10.0)
    
    return psnr

def fsc_stacks(STACK1, STACK2):
    
    fsc_score = []
    img = STACK1
    gt = STACK2
    
    for i in range(img.shape[0]):
        fsc_temp = get_fsc_2d(gt[i], img[i], 1)[1] 
        fsc_score.append(fsc_temp)
        
    return np.asarray(fsc_score)