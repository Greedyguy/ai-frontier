# Dense Video Understanding with Gated Residual Tokenization

**Korean Title:** 조밀한 비디오 이해를 위한 게이트 잔여 토큰화

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Haichao Zhang|Haichao Zhang]] [[authors/Wenhao Chai|Wenhao Chai]] [[authors/Shwai He|Shwai He]] [[authors/Ang Li|Ang Li]] [[authors/Yun Fu|Yun Fu]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dense Temporal Information

## 🔗 유사한 논문
- [[WorldForge_ Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance_20250919|WorldForge Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance]] (80.4% similar)
- [[AToken_ A Unified Tokenizer for Vision_20250919|AToken A Unified Tokenizer for Vision]] (80.1% similar)
- [[Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding_20250919|Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding]] (80.1% similar)
- [[UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (79.5% similar)
- [[MovieCORE_ COgnitive REasoning in Movies_20250919|MovieCORE COgnitive REasoning in Movies]] (79.2% similar)

## 📋 저자 정보

**Authors:** Haichao Zhang, Wenhao Chai, Shwai He, Ang Li, Yun Fu

## 📄 Abstract (원문)

High temporal resolution is essential for capturing fine-grained details in
video understanding. However, current video large language models (VLLMs) and
benchmarks mostly rely on low-frame-rate sampling, such as uniform sampling or
keyframe selection, discarding dense temporal information. This compromise
avoids the high cost of tokenizing every frame, which otherwise leads to
redundant computation and linear token growth as video length increases. While
this trade-off works for slowly changing content, it fails for tasks like
lecture comprehension, where information appears in nearly every frame and
requires precise temporal alignment. To address this gap, we introduce Dense
Video Understanding (DVU), which enables high-FPS video comprehension by
reducing both tokenization time and token overhead. Existing benchmarks are
also limited, as their QA pairs focus on coarse content changes. We therefore
propose DIVE (Dense Information Video Evaluation), the first benchmark designed
for dense temporal reasoning. To make DVU practical, we present Gated Residual
Tokenization (GRT), a two-stage framework: (1) Motion-Compensated Inter-Gated
Tokenization uses pixel-level motion estimation to skip static regions during
tokenization, achieving sub-linear growth in token count and compute. (2)
Semantic-Scene Intra-Tokenization Merging fuses tokens across static regions
within a scene, further reducing redundancy while preserving dynamic semantics.
Experiments on DIVE show that GRT outperforms larger VLLM baselines and scales
positively with FPS. These results highlight the importance of dense temporal
information and demonstrate that GRT enables efficient, scalable high-FPS video
understanding.

## 🔍 Abstract (한글 번역)

고해상도의 시간적 해상도는 비디오 이해에서 세밀한 디테일을 포착하는 데 필수적입니다. 그러나 현재의 비디오 대형 언어 모델(VLLM)과 벤치마크는 대부분 균일 샘플링이나 키프레임 선택과 같은 저프레임률 샘플링에 의존하여 밀집한 시간 정보를 버립니다. 이러한 타협은 모든 프레임을 토큰화하는 높은 비용을 피하는데, 이는 비디오 길이가 증가함에 따라 불필요한 계산과 선형적인 토큰 증가로 이어지기 때문입니다. 이 절충안은 천천히 변화하는 콘텐츠에는 효과적이지만, 정보가 거의 모든 프레임에 나타나고 정확한 시간 정렬이 필요한 강의 이해와 같은 작업에는 실패합니다. 이러한 격차를 해결하기 위해, 우리는 토큰화 시간과 토큰 오버헤드를 줄여 고FPS 비디오 이해를 가능하게 하는 Dense Video Understanding (DVU)을 소개합니다. 기존의 벤치마크는 QA 쌍이 대략적인 콘텐츠 변화에 초점을 맞추고 있어 제한적입니다. 따라서 우리는 밀집한 시간적 추론을 위해 설계된 첫 번째 벤치마크인 DIVE (Dense Information Video Evaluation)를 제안합니다. DVU를 실용적으로 만들기 위해, 우리는 Gated Residual Tokenization (GRT)을 제시합니다. 이는 두 단계의 프레임워크로 구성됩니다: (1) Motion-Compensated Inter-Gated Tokenization은 픽셀 수준의 모션 추정을 사용하여 토큰화 중 정적 영역을 건너뛰어 토큰 수와 계산의 서브-선형 성장을 달성합니다. (2) Semantic-Scene Intra-Tokenization Merging은 장면 내 정적 영역 간의 토큰을 융합하여 동적 의미를 유지하면서 중복을 더욱 줄입니다. DIVE에 대한 실험은 GRT가 더 큰 VLLM 기준선을 능가하며 FPS와 긍정적으로 확장됨을 보여줍니다. 이러한 결과는 밀집한 시간 정보의 중요성을 강조하며, GRT가 효율적이고 확장 가능한 고FPS 비디오 이해를 가능하게 함을 입증합니다.

## 📝 요약

이 논문은 고해상도 영상 이해를 위해 Dense Video Understanding (DVU)을 제안합니다. 기존의 영상 대형 언어 모델(VLLMs)은 낮은 프레임 속도로 인해 세밀한 시간 정보를 놓치는 문제를 해결하기 위해, Gated Residual Tokenization (GRT)이라는 두 단계의 프레임워크를 도입합니다. 첫 번째 단계는 Motion-Compensated Inter-Gated Tokenization으로, 픽셀 수준의 움직임 추정을 통해 정적인 영역을 건너뛰어 토큰 수와 계산량을 줄입니다. 두 번째 단계는 Semantic-Scene Intra-Tokenization Merging으로, 장면 내 정적 영역의 토큰을 병합하여 중복을 줄이면서 동적 의미를 보존합니다. DIVE라는 새로운 벤치마크를 통해 실험한 결과, GRT는 기존 VLLM보다 뛰어난 성능을 보이며, 높은 FPS에서도 효율적이고 확장 가능한 영상 이해를 가능하게 합니다.

## 🎯 주요 포인트

- 1. 현재의 비디오 대형 언어 모델(VLLMs)은 낮은 프레임 속도 샘플링에 의존하여 세밀한 시간 정보를 놓치고 있다.

- 2. 강의 이해와 같은 작업에서는 거의 모든 프레임에 정보가 나타나므로 정확한 시간 정렬이 필요하다.

- 3. Dense Video Understanding(DVU)는 높은 FPS 비디오 이해를 가능하게 하며, 토큰화 시간과 토큰 오버헤드를 줄인다.

- 4. DIVE는 밀도 높은 시간적 추론을 위한 최초의 벤치마크로, 기존 벤치마크의 한계를 극복한다.

- 5. Gated Residual Tokenization(GRT)는 정적 영역을 건너뛰고, 장면 내 정적 영역의 토큰을 융합하여 효율적인 고FPS 비디오 이해를 가능하게 한다.

---

*Generated on 2025-09-20 07:43:04*