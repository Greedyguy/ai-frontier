---
keywords:
  - Transformer Architecture
  - Attention Mechanism
  - Image Super-Resolution
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2401.00241
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:40:12.739506",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer Architecture",
    "Attention Mechanism",
    "Image Super-Resolution"
  ],
  "rejected_keywords": [
    "Local-Global Feature Aggregation"
  ],
  "similarity_scores": {
    "Transformer Architecture": 0.8,
    "Attention Mechanism": 0.78,
    "Image Super-Resolution": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Image Super-Resolution Reconstruction Network based on Enhanced Swin Transformer via Alternating Aggregation of Local-Global Features

**Korean Title:** 강화된 스윈 변환기를 기반으로 한 이미지 초해상도 복원 네트워크: 지역-전역 특징의 교차 집계를 통한 접근

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Transformer Architecture|Swin Transformer]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Image Super-Resolution|Image Super-Resolution]]

## 🔗 유사한 논문
- [[NDLPNet A Location-Aware Nighttime Deraining Network and a Real-World Benchmark Dataset]] (78.5% similar)
- [[Utilizing Novelty-based Evolution Strategies to Train Transformers in Reinforcement Learning]] (78.0% similar)
- [[Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (78.0% similar)
- [[Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (76.9% similar)
- [[Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (76.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2401.00241v5 Announce Type: replace 
Abstract: The Swin Transformer image super-resolution (SR) reconstruction network primarily depends on the long-range relationship of the window and shifted window attention to explore features. However, this approach focuses only on global features, ignoring local ones, and considers only spatial interactions, disregarding channel and spatial-channel feature interactions, limiting its nonlinear mapping capability. Therefore, this study proposes an enhanced Swin Transformer network (ESTN) that alternately aggregates local and global features. During local feature aggregation, shift convolution facilitates the interaction between local spatial and channel information. During global feature aggregation, a block sparse global perception module is introduced, wherein spatial information is reorganized and the recombined features are then processed by a dense layer to achieve global perception. Additionally, multiscale self-attention and low-parameter residual channel attention modules are introduced to aggregate information across different scales. Finally, the effectiveness of ESTN on five public datasets and a local attribution map (LAM) are analyzed. Experimental results demonstrate that the proposed ESTN achieves higher average PSNR, surpassing SRCNN, ELAN-light, SwinIR-light, and SMFANER+ models by 2.17dB, 0.13dB, 0.12dB, and 0.1dB, respectively, with LAM further confirming its larger receptive field. ESTN delivers improved quality of SR images. The source code can be found at https://github.com/huangyuming2021/ESTN.

## 🔍 Abstract (한글 번역)

arXiv:2401.00241v5 발표 유형: 교체  
초록: Swin Transformer 이미지 초해상도(SR) 재구성 네트워크는 주로 윈도우와 시프트 윈도우 주의(attention)의 장거리 관계에 의존하여 특징을 탐색합니다. 그러나 이 접근법은 전역 특징에만 집중하고, 지역적 특징을 무시하며, 공간적 상호작용만 고려하고 채널 및 공간-채널 특징 상호작용을 무시하여 비선형 매핑 능력을 제한합니다. 따라서 본 연구에서는 지역 및 전역 특징을 번갈아 집계하는 향상된 Swin Transformer 네트워크(ESTN)를 제안합니다. 지역 특징 집계 동안, 시프트 컨볼루션은 지역 공간 및 채널 정보 간의 상호작용을 촉진합니다. 전역 특징 집계 동안에는 블록 희소 전역 인식 모듈이 도입되어 공간 정보가 재구성되고, 재구성된 특징은 밀집층에 의해 처리되어 전역 인식을 달성합니다. 또한, 다중 스케일 자기 주의 및 저-파라미터 잔여 채널 주의 모듈이 도입되어 다양한 스케일에 걸쳐 정보를 집계합니다. 마지막으로, 다섯 개의 공공 데이터셋과 지역 속성 맵(LAM)에 대한 ESTN의 효과를 분석합니다. 실험 결과, 제안된 ESTN은 평균 PSNR이 더 높아 SRCNN, ELAN-light, SwinIR-light, SMFANER+ 모델을 각각 2.17dB, 0.13dB, 0.12dB, 0.1dB 초과하며, LAM은 더 큰 수용 영역을 확인합니다. ESTN은 SR 이미지의 품질을 향상시킵니다. 소스 코드는 https://github.com/huangyuming2021/ESTN에서 찾을 수 있습니다.

## 📝 요약

이 연구는 Swin Transformer 기반의 이미지 초해상도(SR) 재구성 네트워크의 한계를 극복하기 위해 개선된 Swin Transformer 네트워크(ESTN)를 제안합니다. 기존 방법이 글로벌 특징에만 집중하고 지역적 및 채널 간 상호작용을 무시하는 문제를 해결하기 위해, ESTN은 지역 및 글로벌 특징을 번갈아 집계합니다. 지역 특징 집계 시, 시프트 컨볼루션을 통해 지역 공간 및 채널 정보의 상호작용을 촉진하며, 글로벌 특징 집계 시 블록 희소 글로벌 인식 모듈을 도입하여 공간 정보를 재구성합니다. 또한, 다중 스케일 자기 주의 및 저매개변수 잔여 채널 주의 모듈을 도입하여 다양한 스케일의 정보를 집계합니다. 실험 결과, ESTN은 다섯 개의 공공 데이터셋에서 평균 PSNR이 기존 모델들보다 최대 2.17dB 높아졌으며, LAM 분석을 통해 더 큰 수용 영역을 확인했습니다. ESTN은 SR 이미지의 품질을 향상시킵니다. 소스 코드는 https://github.com/huangyuming2021/ESTN에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. Swin Transformer 기반 이미지 초해상도 네트워크의 한계를 극복하기 위해, 본 연구는 지역 및 전역 특징을 교대로 집계하는 향상된 Swin Transformer 네트워크(ESTN)를 제안합니다.

- 2. 지역 특징 집계 시, 시프트 컨볼루션을 통해 지역 공간 및 채널 정보 간의 상호작용을 촉진합니다.

- 3. 전역 특징 집계 시, 블록 희소 전역 인식 모듈을 도입하여 공간 정보를 재구성하고, 조합된 특징을 밀집층에서 처리하여 전역 인식을 달성합니다.

- 4. 다중 스케일 자기 주의 및 저매개변수 잔여 채널 주의 모듈을 도입하여 다양한 스케일의 정보를 집계합니다.

- 5. 실험 결과, 제안된 ESTN은 평균 PSNR에서 SRCNN, ELAN-light, SwinIR-light, SMFANER+ 모델을 각각 2.17dB, 0.13dB, 0.12dB, 0.1dB 초과하며, LAM 분석을 통해 더 큰 수용 영역을 확인했습니다.

---

*Generated on 2025-09-19 16:14:21*