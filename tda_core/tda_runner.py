#!/home/tops/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sts=4:sw=4:et:fenc=utf8
import tensorflow as tf
from scheduler.distributed_scheduler import DistributedScheduler

tf.app.flags.DEFINE_string("model_name","HhinModel","model ")
tf.app.flags.DEFINE_integer("batch_size", 256, "batch size")
tf.app.flags.DEFINE_integer("predict_batch_size", 256, "predict batch size")
tf.app.flags.DEFINE_string("transform_json", "conf_fc_hhin.json", "feature transform config json file name")
tf.app.flags.DEFINE_integer("summary_step", 100, "how many steps summary written")
tf.app.flags.DEFINE_integer("print_step", 100, "how many steps print info")
tf.app.flags.DEFINE_integer("train_step", 200000, "train step of running.")
tf.app.flags.DEFINE_integer("checkpoint_step", 100, "how many steps summary written")
tf.app.flags.DEFINE_integer("checkpoint_sec", 600, "checkpoint save seconds.")
tf.app.flags.DEFINE_float("dnn_lr", 0.001, "learning rate for deep part")
tf.app.flags.DEFINE_integer("lr_decay_steps", 400000, "learning rate decay steps")
tf.app.flags.DEFINE_float("lr_decay_rate", 0.99, "learning rate decay rate")
tf.app.flags.DEFINE_float("dnn_l1_weight", 0.0, "l1 regularization weight for deep part")
tf.app.flags.DEFINE_float("dnn_l2_weight", 0.0, "l2 regularization weight for deep part")
tf.app.flags.DEFINE_float("cart_loss_weight", 0.0, "loss weight for cart sample")
tf.app.flags.DEFINE_float("pay_loss_weight", 0.0, "loss weight for pay sample")
tf.app.flags.DEFINE_string("item_hidden_units", "128,128,32", "")
tf.app.flags.DEFINE_string("user_hidden_units", "128,128,32", "")
tf.app.flags.DEFINE_string("dnn_activation", "leaky_relu", "")
tf.app.flags.DEFINE_integer("num_epoch", 8, "epoch used of training data")
tf.app.flags.DEFINE_float("lr_min",0.001,"lr_min")
tf.app.flags.DEFINE_string("lr_op","lr_warm_restart","lr_op")
tf.app.flags.DEFINE_integer("ubb_pos_slice_len",20,"ubb_pos_slice_len")
tf.app.flags.DEFINE_integer("attention_num_units",16,"attention_num_units")
tf.app.flags.DEFINE_integer("attention_num_output_units",16,"attention_num_output_units")
tf.app.flags.DEFINE_string("attention_num_units_forward",'16,16',"")
tf.app.flags.DEFINE_float("drop_out",0.2,"drop_out")
tf.app.flags.DEFINE_string("ubb_combiner", "max,sum", "ubb_combiner")
tf.app.flags.DEFINE_integer("ubb_dim", 8, "ubb_dim")
tf.app.flags.DEFINE_integer("target_comp_dim",8,"target_comp_dim")
tf.app.flags.DEFINE_integer("target_comp_num",4,"target_comp_num")
tf.app.flags.DEFINE_integer("user_emb_num",16,"user_emb_num")
tf.app.flags.DEFINE_integer("gru_group_num_units",16,"gru_group_num_units")
tf.app.flags.DEFINE_float("rate_for_uuloss",0.0001,"rate_for_uuloss")
tf.app.flags.DEFINE_float("rate_for_recloss",0.0001,"rate_for_recloss")
tf.app.flags.DEFINE_integer("group_embedding_num",16,"group_embedding_num")
tf.app.flags.DEFINE_integer("groups_num",5,"groups_num")
tf.app.flags.DEFINE_string("clip_gradients", "true", "true/false")
tf.app.flags.DEFINE_string("checkpoint_dir", "../ctr/test/", "checkpoint dir")
tf.app.flags.DEFINE_string("running_mode", "train", "running mode: train/predict")
tf.app.flags.DEFINE_integer("logits_dimension", 1, "final logits dimension")
tf.app.flags.DEFINE_float("ema_decay", 0.999, "exponential moving average decay for loss")
tf.app.flags.DEFINE_string("decision_layer_units","256,128,32","decision_layer_units")
tf.app.flags.DEFINE_string("model_num",None,"model_num")


# tf.app.flags.DEFINE_integer("fg_capacity",3,"fg_capacity")
# tf.app.flags.DEFINE_integer("fg_thread",8,"fg_thread")
# tf.app.flags.DEFINE_integer("embedding_partition_size", 8388608, "embedding_partition_size")
# tf.app.flags.DEFINE_integer("ubb_feature_num",12,"ubb_feature_num")
# tf.app.flags.DEFINE_integer("ubb_feature_num_side",36,"ubb_feature_num_side")
# tf.app.flags.DEFINE_integer("ubb_dim_side", 16, "ubb_dim_side")
# tf.app.flags.DEFINE_string("hard_att_units","128,64,32","hard_att_units")
# tf.app.flags.DEFINE_integer("heads_num",4,"heads_num")
# tf.app.flags.DEFINE_integer("ubb_feature_unin_num",12,"ubb_feature_unin_num")
# tf.app.flags.DEFINE_integer("ubb_feature_num_neg",4,"ubb_feature_num_neg")
# tf.app.flags.DEFINE_string("uig_pos_layer_units","128,64,64","uig_pos_layer_units")
# tf.app.flags.DEFINE_string("uig_neg_layer_units","128,64,64","uig_neg_layer_units")
# tf.app.flags.DEFINE_integer("ubb_neg_slice_len",20,"ubb_neg_slice_len")
# tf.app.flags.DEFINE_integer("ubb_pyrimid_fc_unit",128,"ubb_pyrimid_fc_unit")
# tf.app.flags.DEFINE_integer("exp_num",8,"exp_num")
# tf.app.flags.DEFINE_integer("ufc_output_num",128,"ufc_output_num")
# tf.app.flags.DEFINE_integer("ufc_forward_num",256,"ufc_forward_num")
# tf.app.flags.DEFINE_integer("task_cnt",2,"task_cnt")
# tf.app.flags.DEFINE_string("group_neg_forward_layer_units","128,128","group_neg_forward_layer_units")
# tf.app.flags.DEFINE_integer("user_neg_emb_num",64,"user_neg_emb_num")
# tf.app.flags.DEFINE_integer("user_seq_emb_num",256,"user_seq_emb_num")
# tf.app.flags.DEFINE_integer("top_num",100,"top_num")
# tf.app.flags.DEFINE_integer("attention_num_output_units_i2topu",64,"attention_num_output_units_i2topu")
# tf.app.flags.DEFINE_integer("attention_num_output_units_u2topu",64,"attention_num_output_units_u2topu")
# tf.app.flags.DEFINE_string("decision_layer_units_for_gate","256,64","decision_layer_units_for_gate")
# tf.app.flags.DEFINE_string("auxiliary_loss_layer_units","256,64","auxiliary_loss_layer_units")

FLAGS = tf.app.flags.FLAGS


def main(_):
    tf.logging.set_verbosity(tf.logging.INFO)
    scheduler = DistributedScheduler()

    if FLAGS.running_mode == "train":
        scheduler.train(FLAGS)
    elif FLAGS.running_mode == "predict":
        scheduler.eval(FLAGS)
    else:
        print("bad running mode: %s" % FLAGS.running_mode)
    return


if __name__ == '__main__':
    tf.app.run()
