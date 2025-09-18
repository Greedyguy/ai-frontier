
# Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection

**Korean Title:** 일반화 가능한 오디오 딥페이크 탐지를 위한 저랭크 어댑터 전문가 혼합체

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Out-of-Domain Scenario|Out-of-Domain Scenario]] [[keywords/broad/Wav2Vec2|Wav2Vec2]] [[keywords/broad/LoRA|LoRA]] [[keywords/specific/Routing Mechanism|Routing Mechanism]] [[keywords/unique/Mixture-of-LoRA-Experts|Mixture-of-LoRA-Experts]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Generalizable Audio Deepfake Detection
**🔬 Broad Technical**: Wav2Vec2, LoRA
**🔗 Specific Connectable**: Fine-tuning
**⭐ Unique Technical**: MoE-LoRA

**ArXiv ID**: [2509.13878](https://arxiv.org/abs/2509.13878)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13878.pdf)


## 🏷️ 추출된 키워드



`Wav2Vec2` • 

`LoRA` • 

`Mixture-of-LoRA-experts` • 

`MoE-LoRA` • 

`Generalizable Audio Deepfake Detection`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13878v1 Announce Type: cross 
Abstract: Foundation models such as Wav2Vec2 excel at representation learning in speech tasks, including audio deepfake detection. However, after being fine-tuned on a fixed set of bonafide and spoofed audio clips, they often fail to generalize to novel deepfake methods not represented in training. To address this, we propose a mixture-of-LoRA-experts approach that integrates multiple low-rank adapters (LoRA) into the model's attention layers. A routing mechanism selectively activates specialized experts, enhancing adaptability to evolving deepfake attacks. Experimental results show that our method outperforms standard fine-tuning in both in-domain and out-of-domain scenarios, reducing equal error rates relative to baseline models. Notably, our best MoE-LoRA model lowers the average out-of-domain EER from 8.55\% to 6.08\%, demonstrating its effectiveness in achieving generalizable audio deepfake detection.

## 🔍 Abstract (한글 번역)

arXiv:2509.13878v1 발표 유형: 교차
요약: Wav2Vec2와 같은 기초 모델은 음성 작업에서 표현 학습에서 뛰어나며 오디오 딥페이크 감지를 포함합니다. 그러나 공식 및 가짜 오디오 클립의 고정된 세트에서 미세 조정된 후, 종종 훈련 중에 나타나지 않은 새로운 딥페이크 방법에 대한 일반화에 실패합니다. 이를 해결하기 위해, 우리는 모델의 주의 레이어에 여러 개의 저랭크 어댑터(LoRA)를 통합하는 LoRA 전문가의 혼합 접근 방식을 제안합니다. 라우팅 메커니즘은 전문가를 선택적으로 활성화하여 진화하는 딥페이크 공격에 대한 적응성을 향상시킵니다. 실험 결과는 우리의 방법이 도메인 내 및 도메인 외 시나리오에서 표준 미세 조정보다 우수함을 보여주며, 베이스라인 모델에 비해 동등 오류율을 줄입니다. 특히, 최고의 MoE-LoRA 모델은 도메인 외 EER의 평균을 8.55\%에서 6.08\%로 낮추어 일반화된 오디오 딥페이크 감지를 달성하는 효과를 보여줍니다.

## 📝 요약

한국어 요약:
Wav2Vec2와 같은 Foundation 모델은 음성 작업에서 탁월한 표현 학습을 수행하지만, 고정된 진짜 및 가짜 오디오 클립 세트에서 미세 조정된 후에는 훈련에 표현되지 않은 새로운 딥페이크 방법에 대해 일반화하는 데 실패할 수 있습니다. 이를 해결하기 위해 저희는 여러 Low-rank Adapter (LoRA)를 모델의 attention 레이어에 통합하는 MoE-LoRA 접근 방식을 제안합니다. 라우팅 메커니즘은 전문가를 선택적으로 활성화하여 진화하는 딥페이크 공격에 대한 적응성을 향상시킵니다. 실험 결과는 우리의 방법이 기존 모델에 비해 도메인 내 및 도메인 외 시나리오에서 우수한 성능을 보여주며, 기준 모델에 비해 동등 오류율을 줄입니다. 특히, 최고의 MoE-LoRA 모델은 도메인 외 EER을 8.55%에서 6.08%로 낮추어 일반화된 오디오 딥페이크 감지의 효과를 입증합니다.

## 🎯 주요 포인트


- Wav2Vec2 모델은 음성 작업에서 탁월한 표현 학습을 수행한다.

- 새로운 딥페이크 방법에 대해 일반화하기 어려운 문제를 해결하기 위해 LoRA 전문가의 혼합 방법을 제안한다.

- 실험 결과는 MoE-LoRA 모델이 기존 모델에 비해 성능이 우수하며 일반화된 오디오 딥페이크 감지를 달성한다.


---

*Generated on 2025-09-18 16:44:40*