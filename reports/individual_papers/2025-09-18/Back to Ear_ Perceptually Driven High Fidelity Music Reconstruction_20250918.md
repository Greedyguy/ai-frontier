# Back to Ear: Perceptually Driven High Fidelity Music Reconstruction

**Korean Title:** 귀로 돌아가기: 지각적으로 구동되는 고충실도 음악 재구성

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Kangdi Wang|Kangdi Wang]] [[authors/Zhiyue Wu|Zhiyue Wu]] [[authors/Dinghao Zhou|Dinghao Zhou]] [[authors/Rui Lin|Rui Lin]] [[authors/Junyu Dai|Junyu Dai]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Perceptual Filter

## 🔗 유사한 논문
- [[Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing_20250918|Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing]] (78.5% similar)
- [[Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance_20250919|Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance]] (77.7% similar)
- [[Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation_20250919|Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation]] (77.7% similar)
- [[Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (77.5% similar)
- [[Listening, Imagining & Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining & Refining A Heuristic Optimized ASR Correction Framework with LLMs]] (77.1% similar)

## 📋 저자 정보

**Authors:** Kangdi Wang, Zhiyue Wu, Dinghao Zhou, Rui Lin, Junyu Dai, Tao Jiang

## 📄 Abstract (원문)

Variational Autoencoders (VAEs) are essential for large-scale audio tasks
like diffusion-based generation. However, existing open-source models often
neglect auditory perceptual aspects during training, leading to weaknesses in
phase accuracy and stereophonic spatial representation. To address these
challenges, we propose {\epsilon}ar-VAE, an open-source music signal
reconstruction model that rethinks and optimizes the VAE training paradigm. Our
contributions are threefold: (i) A K-weighting perceptual filter applied prior
to loss calculation to align the objective with auditory perception. (ii) Two
novel phase losses: a Correlation Loss for stereo coherence, and a Phase Loss
using its derivatives--Instantaneous Frequency and Group Delay--for precision.
(iii) A new spectral supervision paradigm where magnitude is supervised by all
four Mid/Side/Left/Right components, while phase is supervised only by the LR
components. Experiments show {\epsilon}ar-VAE at 44.1kHz substantially
outperforms leading open-source models across diverse metrics, showing
particular strength in reconstructing high-frequency harmonics and the spatial
characteristics.

## 🔍 Abstract (한글 번역)

변분 오토인코더(VAEs)는 확산 기반 생성과 같은 대규모 오디오 작업에 필수적입니다. 그러나 기존의 오픈 소스 모델들은 훈련 과정에서 청각적 지각 측면을 종종 간과하여 위상 정확성과 입체 음향 공간 표현에서 약점을 드러냅니다. 이러한 문제를 해결하기 위해, 우리는 VAE 훈련 패러다임을 재고하고 최적화한 오픈 소스 음악 신호 재구성 모델인 {\epsilon}ar-VAE를 제안합니다. 우리의 기여는 세 가지로 요약됩니다: (i) 청각적 지각과 목표를 일치시키기 위해 손실 계산 전에 K-가중 지각 필터를 적용합니다. (ii) 두 가지 새로운 위상 손실: 스테레오 일관성을 위한 상관 손실과 정밀성을 위한 순간 주파수 및 군 지연을 사용하는 위상 손실입니다. (iii) 크기는 모든 Mid/Side/Left/Right 구성 요소에 의해 감독되고, 위상은 LR 구성 요소에 의해서만 감독되는 새로운 스펙트럼 감독 패러다임입니다. 실험 결과, 44.1kHz에서 {\epsilon}ar-VAE는 다양한 지표에서 선도적인 오픈 소스 모델들을 크게 능가하며, 특히 고주파 하모닉스와 공간적 특성을 재구성하는 데 강점을 보였습니다.

## 📝 요약

Variational Autoencoders(VAEs)는 대규모 오디오 작업에 필수적이지만, 기존 모델들은 청각적 인식을 간과하여 위상 정확성과 입체적 공간 표현에 약점을 보입니다. 이를 해결하기 위해 {\epsilon}ar-VAE를 제안합니다. 주요 기여는 다음과 같습니다: (i) 청각 인식과 일치시키기 위한 K-가중치 지각 필터 적용, (ii) 스테레오 일관성을 위한 상관 손실과 정밀성을 위한 위상 손실 도입, (iii) 새로운 스펙트럼 감독 패러다임으로, 실험 결과 {\epsilon}ar-VAE는 고주파 하모닉스와 공간적 특성 재구성에서 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 기존 오픈소스 모델의 한계를 극복하기 위해 청각적 지각을 고려한 K-weighting 지각 필터를 손실 계산 전에 적용합니다.

- 2. 스테레오 일관성을 위한 상관 손실과 정밀성을 위한 순간 주파수 및 군 지연을 활용한 새로운 위상 손실을 제안합니다.

- 3. 새로운 스펙트럼 감독 패러다임을 도입하여, 크기는 Mid/Side/Left/Right 모든 구성 요소로 감독하고, 위상은 LR 구성 요소로만 감독합니다.

- 4. 실험 결과, {\epsilon}ar-VAE는 44.1kHz에서 다양한 지표에서 기존 오픈소스 모델을 능가하며, 특히 고주파 하모닉 및 공간적 특성 재구성에서 강점을 보입니다.

---

*Generated on 2025-09-20 02:44:12*