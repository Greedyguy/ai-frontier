
# Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production

**Korean Title:** 실시간 수어 생성용 하이브리드 자기회귀-확산 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Hybrid Autoregressive-Diffusion Model

## 🔗 유사한 논문
- [[SSL-SSAW Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation]] (82.8% similar)
- [[Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech_20250919|Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech]] (81.6% similar)
- [[Kling-Avatar Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis]] (81.6% similar)
- [[DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (80.4% similar)
- [[Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.09105v3 Announce Type: replace 
Abstract: Earlier Sign Language Production (SLP) models typically relied on autoregressive methods that generate output tokens one by one, which inherently provide temporal alignment. Although techniques like Teacher Forcing can prevent model collapse during training, they still cannot solve the problem of error accumulation during inference, since ground truth is unavailable at that stage. In contrast, more recent approaches based on diffusion models leverage step-by-step denoising to enable high-quality generation. However, the iterative nature of these models and the requirement to denoise entire sequences limit their applicability in real-time tasks like SLP. To address it, we explore a hybrid approach that combines autoregressive and diffusion models for SLP, leveraging the strengths of both models in sequential dependency modeling and output refinement. To capture fine-grained body movements, we design a Multi-Scale Pose Representation module that separately extracts detailed features from distinct articulators and integrates them via a Multi-Scale Fusion module. Furthermore, we introduce a Confidence-Aware Causal Attention mechanism that utilizes joint-level confidence scores to dynamically guide the pose generation process, improving accuracy and robustness. Extensive experiments on the PHOENIX14T and How2Sign datasets demonstrate the effectiveness of our method in both generation quality and real-time efficiency.

## 🔍 Abstract (한글 번역)

arXiv:2507.09105v3 발표 유형: 교체  
초록: 초기 수어 생성(SLP) 모델은 일반적으로 출력 토큰을 하나씩 생성하는 자기회귀 방법에 의존했으며, 이는 본질적으로 시간적 정렬을 제공합니다. 교사 강제(Teacher Forcing)와 같은 기법은 훈련 중 모델 붕괴를 방지할 수 있지만, 추론 단계에서는 정답이 없기 때문에 오류 누적 문제를 해결할 수 없습니다. 반면에, 최근의 확산 모델 기반 접근 방식은 단계별 노이즈 제거를 통해 고품질 생성을 가능하게 합니다. 그러나 이러한 모델의 반복적 특성과 전체 시퀀스를 노이즈 제거해야 하는 요구사항은 SLP와 같은 실시간 작업에서의 적용 가능성을 제한합니다. 이를 해결하기 위해, 우리는 자기회귀 모델과 확산 모델을 결합한 하이브리드 접근 방식을 탐구하여, 순차적 종속성 모델링과 출력 정제에서 두 모델의 강점을 활용합니다. 세밀한 신체 움직임을 포착하기 위해, 우리는 서로 다른 관절에서 세부적인 특징을 개별적으로 추출하고 이를 다중 스케일 융합 모듈을 통해 통합하는 다중 스케일 자세 표현 모듈을 설계했습니다. 또한, 관절 수준의 신뢰도 점수를 활용하여 자세 생성 과정을 동적으로 안내함으로써 정확성과 견고성을 향상시키는 신뢰도 인식 인과적 주의 메커니즘을 도입했습니다. PHOENIX14T 및 How2Sign 데이터셋에 대한 광범위한 실험은 생성 품질과 실시간 효율성 모두에서 우리의 방법의 효과를 입증합니다.

## 📝 요약

이 논문은 수어 생성(SLP) 모델에서의 새로운 접근법을 제안합니다. 기존의 자회귀 모델은 시간 정렬을 제공하지만, 오류 누적 문제를 해결하지 못했습니다. 최근의 확산 모델은 고품질 생성을 가능하게 하지만, 실시간 작업에는 한계가 있습니다. 본 연구는 자회귀 모델과 확산 모델을 결합한 하이브리드 접근법을 통해 이러한 문제를 해결하고자 합니다. 세밀한 신체 움직임을 포착하기 위해 다중 스케일 자세 표현 모듈을 설계하고, 자신감 인식 인과주의 주의 메커니즘을 도입하여 자세 생성의 정확성과 견고성을 향상시켰습니다. PHOENIX14T와 How2Sign 데이터셋을 활용한 실험 결과, 제안된 방법이 생성 품질과 실시간 효율성에서 우수함을 입증했습니다.

## 🎯 주요 포인트

- 1. 기존 수어 생성 모델은 순차적으로 출력을 생성하는 자기회귀 방식을 사용하여 시간적 정렬을 제공했으나, 오류 누적 문제를 해결하지 못했습니다.

- 2. 최근 확산 모델 기반 접근법은 단계별 노이즈 제거를 통해 고품질 생성을 가능하게 하지만, 실시간 작업에는 한계가 있습니다.

- 3. 자기회귀 모델과 확산 모델을 결합한 하이브리드 접근법을 통해 순차적 의존성 모델링과 출력 정제를 동시에 활용합니다.

- 4. 세밀한 신체 움직임을 포착하기 위해 Multi-Scale Pose Representation 모듈을 설계하여 다양한 관절에서 세부 특징을 추출하고 통합합니다.

- 5. Confidence-Aware Causal Attention 메커니즘을 도입하여 관절 수준의 신뢰도 점수를 활용해 자세 생성 과정을 동적으로 안내함으로써 정확성과 견고성을 향상시킵니다.

---

*Generated on 2025-09-19 16:18:09*