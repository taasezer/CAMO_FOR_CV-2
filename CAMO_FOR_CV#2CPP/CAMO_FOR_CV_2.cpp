#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdexcept>

extern "C" {
    __declspec(dllexport) void captureVideo(const std::string& outputPath) {
        try {
            cv::VideoCapture cap(0);
            if (!cap.isOpened()) {
                throw std::runtime_error("Kamera açılamadı!");
            }

            cv::Mat frame;
            cv::VideoWriter writer(outputPath, cv::VideoWriter::fourcc('M','J','P','G'), 30, cv::Size(640, 480));

            while (true) {
                cap >> frame;
                if (frame.empty()) {
                    throw std::runtime_error("Boş frame alındı!");
                }

                writer.write(frame);
                cv::imshow("Kamera Görüntüsü", frame);
                if (cv::waitKey(1) == 'q') {
                    break;
                }
            }

            cap.release();
            writer.release();
            cv::destroyAllWindows();
        } catch (const std::exception& e) {
            std::cerr << "Hata: " << e.what() << std::endl;
        }
    }
}
