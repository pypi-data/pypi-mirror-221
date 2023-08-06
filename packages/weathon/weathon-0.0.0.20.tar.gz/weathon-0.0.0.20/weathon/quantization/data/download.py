from weathon.quantization.data.tick_data import TencentTickDown, SinaTickDown, NetEasyTickDown


def download_tick_data():
    tencent_dwonloader = TencentTickDown("./")


    tencent_dwonloader.run()


if __name__ == '__main__':
    download_tick_data()