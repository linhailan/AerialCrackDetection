from keras import backend as K


class Config:

    def __init__(self):
        self.verbose = True

        # setting for data augmentation
        # augment with horizontal flips in training
        self.use_horizontal_flips = False
        # Augment with vertical flips in training
        self.use_vertical_flips = False
        # Augment with 90 degree rotations in training
        self.rot_90 = False

        # Location to store all the metadata related to the training (to be used when testing).
        self.config_filename = "config.pickle"

        # anchor box scales
        self.anchor_box_scales = [128, 256, 512]

        # anchor box ratios
        self.anchor_box_ratios = [[1, 1], [1, 2], [2, 1]]

        # size to resize the smallest side of the image
        self.im_size = 600

        # image channel-wise mean to subtract
        self.img_channel_mean = [103.939, 116.779, 123.68]
        self.img_scaling_factor = 1.0

        # number of ROIs per iteration, higher means more memory use.
        self.batch_size = 16

        self.num_epochs = 2000

        # stride at the RPN (this depends on the network configuration)
        self.rpn_stride = 16

        self.balanced_classes = False

        # scaling the stdev
        self.std_scaling = 4.0
        self.classifier_regr_std = [8.0, 8.0, 4.0, 4.0]

        # overlaps for RPN
        self.rpn_min_overlap = 0.3
        self.rpn_max_overlap = 0.7

        # overlaps for classifier ROIs
        self.classifier_min_overlap = 0.1
        self.classifier_max_overlap = 0.5

        self.model_path = './model_frcnn.hdf5'

        # placeholder for the class mapping, automatically generated by the parser
        self.class_mapping = None