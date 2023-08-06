import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class SSPQDD(object):
    def __init__(self):
        self.model = tf.lite.Interpreter(model_path='models\converted_model.tflite')
        self.model.allocate_tensors()
        self.input_details = self.model.get_input_details()
        self.output_details = self.model.get_output_details()

    def pre_process(self, sig, maxim, minim):
        new = [np.max(sig[i:i+10]) for i in range(0, len(sig), 10)]
        sig_norm = [(2 / (maxim - minim)) * val for val in new]
        signal = np.array(sig_norm)
        signal.shape = tuple(self.input_details[0]['shape'])
        return signal

    def infer(self, sig, num_grid=188):
        self.model.set_tensor(self.input_details[0]['index'], np.asarray(sig).astype('float32'))
        self.model.invoke()
        class_out = self.model.get_tensor(self.output_details[0]['index'])
        conf_out = self.model.get_tensor(self.output_details[1]['index'])
        pred_conf = np.array(tf.transpose(conf_out)).reshape(2, num_grid)
        pred_class = np.array(tf.transpose(class_out)).reshape(6, num_grid)
        return pred_class, pred_conf

    def post_process(self, class_out, conf_out):
        ind = [i for i, x in enumerate(conf_out[0]) if x > 0.95]
        boxes = []
        try:
            start = ind[0]
            for i in range(len(ind)):
                if i + 1 < len(ind) and ind[i + 1] - ind[i] == 1:
                    continue
                block = {'start': start * 16, 'stop': (ind[i] + 1) * 16, 'class': np.argmax(class_out[:, start])}
                boxes.append(block)
                if i + 1 < len(ind):
                    start = ind[i + 1]
            return boxes, np.argmax(class_out[:, ind[0]])
        except IndexError:
            return boxes, []

if __name__ == '__main__':
    time = np.arange(0, 3.75, 1 / 8000)
    amplitude = np.roll(10 * np.sin(2 * 50 * np.pi * time), 500)
    amplitude[1600:1600 + 16000] = 0.2 * amplitude[1600:1600 + 16000]
    amplitude[6400:6400 + 16000] = 1.2 * amplitude[6400:6400 + 16000]
    ind = 1600
    impulse = 9
    amplitude[ind] = impulse
    sspqdd = SSPQDD()
    sig = sspqdd.pre_process(amplitude, 10, -10)
    class_out, conf_out = sspqdd.infer(sig)
    boxes, ind_class = sspqdd.post_process(class_out, conf_out)

    fig, axs = plt.subplots(4)
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'black']

    axs[0].plot(10 * np.reshape(sig, 3000))
    axs[0].set_xlim([0, 3000])
    axs[0].set_ylim([-15, 15])
    for i in range(len(boxes)):
        rect = plt.Rectangle((boxes[i]['start'], 12.5), boxes[i]['stop'] - boxes[i]['start'], -25, linewidth=1,
                             edgecolor=colors[boxes[i]['class']], facecolor='none', zorder=2)
        axs[0].add_patch(rect)

    axs[1].plot(amplitude)
    axs[1].set_xlim([0, len(amplitude)])
    axs[1].set_ylim([-15, 15])
    for i in range(len(boxes)):
        rect = plt.Rectangle((boxes[i]['start'] * 10, 12.5), boxes[i]['stop'] * 10 - boxes[i]['start'] * 10, -25,
                             linewidth=1, edgecolor=colors[boxes[i]['class']], facecolor='none', zorder=2)
        axs[1].add_patch(rect)

    axs[2].imshow(conf_out, extent=[-1, 1880, -1, 140], cmap='cividis', interpolation='nearest')
    axs[3].imshow(class_out, extent=[-1, 1880, -1, 140], cmap='cividis', interpolation='nearest')
    plt.show()
