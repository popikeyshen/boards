#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: popikeyshen
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import osmosdr
import time
from gnuradio import qtgui

class block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "block")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.vco_freq = vco_freq = int(1000000)
        self.sample_rate = sample_rate = int(10000000)
        self.Frequency = Frequency = 2400e6
        self.Bandwith = Bandwith = 1e6

        ##################################################
        # Blocks
        ##################################################
        self._Frequency_range = Range(433e6, 5000e6, 1e6, 2400e6, 200)
        self._Frequency_win = RangeWidget(self._Frequency_range, self.set_Frequency, 'Frequency', "slider", float)
        self.top_grid_layout.addWidget(self._Frequency_win)
        self._Bandwith_range = Range(1e5, 20e6, 100000, 1e6, 200)
        self._Bandwith_win = RangeWidget(self._Bandwith_range, self.set_Bandwith, 'Bandwith', "slider", float)
        self.top_grid_layout.addWidget(self._Bandwith_win)
        self.qtgui_sink_x_1_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            sample_rate, #bw
            "out1", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_1_0.set_update_time(1.0/10)
        self._qtgui_sink_x_1_0_win = sip.wrapinstance(self.qtgui_sink_x_1_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_1_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_1_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            sample_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(2) + " " + 'bladerf=0,nchan=2'
        )
        self.osmosdr_source_0.set_time_now(osmosdr.time_spec_t(time.time()), osmosdr.ALL_MBOARDS)
        self.osmosdr_source_0.set_sample_rate(sample_rate)
        self.osmosdr_source_0.set_center_freq(Frequency, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_gain(40, 0)
        self.osmosdr_source_0.set_if_gain(40, 0)
        self.osmosdr_source_0.set_bb_gain(40, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(Bandwith, 0)
        self.osmosdr_source_0.set_center_freq(Frequency, 1)
        self.osmosdr_source_0.set_freq_corr(0, 1)
        self.osmosdr_source_0.set_gain(40, 1)
        self.osmosdr_source_0.set_if_gain(40, 1)
        self.osmosdr_source_0.set_bb_gain(40, 1)
        self.osmosdr_source_0.set_antenna('', 1)
        self.osmosdr_source_0.set_bandwidth(Bandwith, 1)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(2) + " " + 'bladerf=0,nchan=2'
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(sample_rate)
        self.osmosdr_sink_0.set_center_freq(Frequency, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(30, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(Bandwith, 0)
        self.osmosdr_sink_0.set_center_freq(Frequency, 1)
        self.osmosdr_sink_0.set_freq_corr(0, 1)
        self.osmosdr_sink_0.set_gain(1, 1)
        self.osmosdr_sink_0.set_if_gain(0, 1)
        self.osmosdr_sink_0.set_bb_gain(0, 1)
        self.osmosdr_sink_0.set_antenna('', 1)
        self.osmosdr_sink_0.set_bandwidth(0, 1)
        self.blocks_vco_c_0 = blocks.vco_c(10e6, 6.28e6, 1)
        self.blocks_udp_sink_0_0 = blocks.udp_sink(gr.sizeof_gr_complex*2, '192.168.92.54', 5000, 1024*4, True)
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*1, 2)
        self.analog_sig_source_x_0 = analog.sig_source_f(sample_rate, analog.GR_SAW_WAVE, 1e3, 1, 0, 0)
        self.analog_agc_xx_0_0 = analog.agc_cc(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0_0.set_max_gain(65536)
        self.analog_agc_xx_0 = analog.agc_cc(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.blocks_streams_to_vector_0, 0))
        self.connect((self.analog_agc_xx_0, 0), (self.qtgui_sink_x_1_0, 0))
        self.connect((self.analog_agc_xx_0_0, 0), (self.blocks_streams_to_vector_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.blocks_streams_to_vector_0, 0), (self.blocks_udp_sink_0_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.osmosdr_sink_0, 1))
        self.connect((self.osmosdr_source_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.osmosdr_source_0, 1), (self.analog_agc_xx_0_0, 0))
        self.connect((self.osmosdr_source_0, 1), (self.qtgui_freq_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_vco_freq(self):
        return self.vco_freq

    def set_vco_freq(self, vco_freq):
        self.vco_freq = vco_freq

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.sample_rate)
        self.osmosdr_sink_0.set_sample_rate(self.sample_rate)
        self.osmosdr_source_0.set_sample_rate(self.sample_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.sample_rate)
        self.qtgui_sink_x_1_0.set_frequency_range(0, self.sample_rate)

    def get_Frequency(self):
        return self.Frequency

    def set_Frequency(self, Frequency):
        self.Frequency = Frequency
        self.osmosdr_sink_0.set_center_freq(self.Frequency, 0)
        self.osmosdr_sink_0.set_center_freq(self.Frequency, 1)
        self.osmosdr_source_0.set_center_freq(self.Frequency, 0)
        self.osmosdr_source_0.set_center_freq(self.Frequency, 1)

    def get_Bandwith(self):
        return self.Bandwith

    def set_Bandwith(self, Bandwith):
        self.Bandwith = Bandwith
        self.osmosdr_sink_0.set_bandwidth(self.Bandwith, 0)
        self.osmosdr_source_0.set_bandwidth(self.Bandwith, 0)
        self.osmosdr_source_0.set_bandwidth(self.Bandwith, 1)



def main(top_block_cls=block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
