
# A Novel Compression Framework for YOLOv8: Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation

**Korean Title:** YOLOv8를 위한 새로운 압축 프레임워크: 구조화된 가지치기와 채널별 증류를 통해 엣지 장치에서 실시간 항공 물체 감지 달성

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Real-Time Deployment|Real-Time Deployment]] [[keywords/broad/Compression|Compression]] [[keywords/broad/Object Detection|Object Detection]] [[keywords/specific/Sparsity-aware Training|Sparsity-aware Training]] [[keywords/unique/Channel-Wise Knowledge Distillation|Channel-Wise Knowledge Distillation]] [[categories/cs.CV|cs.CV]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Real-Time Deployment
**🔬 Broad Technical**: Compression, Object Detection
**🔗 Specific Connectable**: Sparsity-aware Training
**⭐ Unique Technical**: Channel-Wise Knowledge Distillation

**ArXiv ID**: [2509.12918](https://arxiv.org/abs/2509.12918)
**Published**: 2025-09-18
**Category**: cs.CV
**PDF**: [Download](https://arxiv.org/pdf/2509.12918.pdf)


## 🏷️ 추출된 키워드



`Compression` • 

`Object Detection` • 

`Sparsity-aware Training` • 

`Channel-Wise Knowledge Distillation` • 

`Real-Time Deployment`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12918v2 Announce Type: replace 
Abstract: Efficient deployment of deep learning models for aerial object detection on resource-constrained devices requires significant compression without com-promising performance. In this study, we propose a novel three-stage compression pipeline for the YOLOv8 object detection model, integrating sparsity-aware training, structured channel pruning, and Channel-Wise Knowledge Distillation (CWD). First, sparsity-aware training introduces dynamic sparsity during model optimization, effectively balancing parameter reduction and detection accuracy. Second, we apply structured channel pruning by leveraging batch normalization scaling factors to eliminate redundant channels, significantly reducing model size and computational complexity. Finally, to mitigate the accuracy drop caused by pruning, we employ CWD to transfer knowledge from the original model, using an adjustable temperature and loss weighting scheme tailored for small and medium object detection. Extensive experiments on the VisDrone dataset demonstrate the effectiveness of our approach across multiple YOLOv8 variants. For YOLOv8m, our method reduces model parameters from 25.85M to 6.85M (a 73.51% reduction), FLOPs from 49.6G to 13.3G, and MACs from 101G to 34.5G, while reducing AP50 by only 2.7%. The resulting compressed model achieves 47.9 AP50 and boosts inference speed from 26 FPS (YOLOv8m baseline) to 45 FPS, enabling real-time deployment on edge devices. We further apply TensorRT as a lightweight optimization step. While this introduces a minor drop in AP50 (from 47.9 to 47.6), it significantly improves inference speed from 45 to 68 FPS, demonstrating the practicality of our approach for high-throughput, re-source-constrained scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2509.12918v2 발표 유형: 대체
초록: 자원 제약 장치에서 공중 물체 감지를 위한 딥 러닝 모델을 효율적으로 배포하려면 성능을 저하시키지 않고 상당한 압축이 필요합니다. 본 연구에서는 YOLOv8 객체 감지 모델을 위한 새로운 세 단계 압축 파이프라인을 제안합니다. 이는 희소성 인식 훈련, 구조화된 채널 가지치기 및 채널별 지식 증류(CWD)를 통합합니다. 먼저, 희소성 인식 훈련은 모델 최적화 중에 동적 희소성을 도입하여 매개변수 감소와 감지 정확도를 효과적으로 균형있게 유지합니다. 둘째, 우리는 배치 정규화 스케일링 요소를 활용하여 구조화된 채널 가지치기를 적용하여 중복 채널을 제거하고 모델 크기와 계산 복잡성을 크게 줄입니다. 마지막으로, 가지치기로 인한 정확도 하락을 완화하기 위해 CWD를 사용하여 원본 모델로부터 지식을 전달하며, 작은 및 중간 크기의 물체 감지에 맞춘 조절 가능한 온도 및 손실 가중치 체계를 사용합니다. VisDrone 데이터셋에서의 광범위한 실험은 여러 YOLOv8 변형에 대한 접근 방식의 효과를 입증합니다. YOLOv8m의 경우, 우리의 방법은 모델 매개변수를 25.85M에서 6.85M으로 줄이고(73.51% 감소), FLOPs를 49.6G에서 13.3G로, MACs를 101G에서 34.5G로 줄이며, AP50를 2.7%만 감소시킵니다. 결과적으로 압축된 모델은 47.9 AP50을 달성하고 추론 속도를 26 FPS(YOLOv8m 기준)에서 45 FPS로 높여 에지 장치에서 실시간 배포를 가능하게 합니다. 우리는 TensorRT를 가벼운 최적화 단계로 추가적으로 적용합니다. 이로 인해 AP50에서 약간의 감소가 발생하지만(47.9에서 47.6으로), 추론 속도가 45에서 68 FPS로 크게 향상되어 고처리량, 자원 제약 시나리오에 대한 우리 방법의 실용성을 입증합니다.

## 📝 요약

본 연구에서는 자원 제약이 있는 장치에서 공중 물체 감지를 위한 딥 러닝 모델을 효율적으로 배포하기 위해 중요한 압축이 필요하다. 우리는 YOLOv8 객체 감지 모델을 위한 새로운 3단계 압축 파이프라인을 제안한다. 이를 위해 희소성 인식 훈련, 구조화된 채널 가지치기, 그리고 채널별 지식 증류를 통합하였다. 실험 결과, 우리의 방법은 YOLOv8m의 모델 파라미터를 73.51% 줄이고, AP50를 2.7%만 감소시키면서 추론 속도를 26 FPS에서 45 FPS로 향상시켰다. TensorRT를 적용하여 AP50를 약간 감소시키지만 추론 속도를 45 FPS에서 68 FPS로 향상시켜 자원 제약 시나리오에서 우리의 방법의 실용성을 입증하였다.

## 🎯 주요 포인트


- 1. YOLOv8 객체 탐지 모델을 위한 새로운 세 단계 압축 파이프라인 제안

- 2. 제안된 방법은 모델 파라미터를 73.51% 줄이고 추론 속도를 45 FPS로 향상시킴

- 3. TensorRT를 활용한 경량 최적화로 추론 속도를 68 FPS로 더 향상 가능


---

*Generated on 2025-09-18 17:07:45*