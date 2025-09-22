# Generating Moving 3D Soundscapes with Latent Diffusion Models

**Korean Title:** 움직이는 3D 사운드스케이프 생성: 잠재 확산 모델을 활용하여

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Moving Sound Sources

## 🔗 유사한 논문
- [[2025-09-18/Spatial Audio Motion Understanding and Reasoning_20250918|Spatial Audio Motion Understanding and Reasoning]] (84.6% similar)
- [[2025-09-22/FLOAT_ Generative Motion Latent Flow Matching for Audio-driven Talking Portrait_20250922|FLOAT Generative Motion Latent Flow Matching for Audio-driven Talking Portrait]] (83.0% similar)
- [[2025-09-17/RFM-Editing_ Rectified Flow Matching for Text-guided Audio Editing_20250917|RFM-Editing Rectified Flow Matching for Text-guided Audio Editing]] (82.3% similar)
- [[2025-09-19/Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation_20250919|Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation]] (81.2% similar)
- [[2025-09-17/DSpAST_ Disentangled Representations for Spatial Audio Reasoning with Large Language Models_20250917|DSpAST Disentangled Representations for Spatial Audio Reasoning with Large Language Models]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.07318v2 Announce Type: replace-cross 
Abstract: Spatial audio has become central to immersive applications such as VR/AR, cinema, and music. Existing generative audio models are largely limited to mono or stereo formats and cannot capture the full 3D localization cues available in first-order Ambisonics (FOA). Recent FOA models extend text-to-audio generation but remain restricted to static sources. In this work, we introduce SonicMotion, the first end-to-end latent diffusion framework capable of generating FOA audio with explicit control over moving sound sources. SonicMotion is implemented in two variations: 1) a descriptive model conditioned on natural language prompts, and 2) a parametric model conditioned on both text and spatial trajectory parameters for higher precision. To support training and evaluation, we construct a new dataset of over one million simulated FOA caption pairs that include both static and dynamic sources with annotated azimuth, elevation, and motion attributes. Experiments show that SonicMotion achieves state-of-the-art semantic alignment and perceptual quality comparable to leading text-to-audio systems, while uniquely attaining low spatial localization error.

## 🔍 Abstract (한글 번역)

arXiv:2507.07318v2 발표 유형: 교차 대체  
초록: 공간 오디오는 VR/AR, 영화, 음악과 같은 몰입형 응용 프로그램에서 중심적인 역할을 하고 있습니다. 기존의 생성 오디오 모델은 주로 모노 또는 스테레오 형식에 제한되어 있으며, 1차 앰비소닉스(FOA)에서 제공하는 완전한 3D 위치 정보를 포착할 수 없습니다. 최근의 FOA 모델은 텍스트-오디오 생성으로 확장되었지만, 여전히 정적 소스에 제한되어 있습니다. 본 연구에서는 SonicMotion을 소개합니다. 이는 움직이는 소리 소스에 대한 명시적 제어가 가능한 최초의 엔드-투-엔드 잠재 확산 프레임워크로, FOA 오디오를 생성할 수 있습니다. SonicMotion은 두 가지 변형으로 구현됩니다: 1) 자연어 프롬프트에 조건화된 설명적 모델과, 2) 텍스트와 공간 궤적 매개변수에 조건화되어 더 높은 정밀도를 제공하는 파라메트릭 모델입니다. 학습 및 평가를 지원하기 위해, 우리는 정적 및 동적 소스를 포함하고 방위각, 고도, 운동 속성을 주석으로 포함한 100만 개 이상의 시뮬레이션된 FOA 캡션 쌍으로 구성된 새로운 데이터셋을 구축했습니다. 실험 결과, SonicMotion은 최첨단의 의미적 정렬과 지각적 품질을 달성하며, 독창적으로 낮은 공간 위치 오류를 달성하는 것으로 나타났습니다.

## 📝 요약

이 논문에서는 SonicMotion이라는 새로운 프레임워크를 제안합니다. 이는 최초로 움직이는 음원에 대한 명확한 제어가 가능한 FOA(First-Order Ambisonics) 오디오를 생성할 수 있는 잠재 확산 모델입니다. SonicMotion은 자연어 프롬프트에 기반한 설명적 모델과 텍스트 및 공간 궤적 파라미터에 기반한 파라메트릭 모델 두 가지로 구현됩니다. 학습 및 평가를 위해 정적 및 동적 음원에 대한 방위각, 고도, 움직임 속성을 포함한 백만 개 이상의 시뮬레이션된 FOA 캡션 쌍 데이터셋을 구축했습니다. 실험 결과, SonicMotion은 최첨단 의미적 정렬과 지각적 품질을 달성하며, 특히 낮은 공간 위치 오차를 통해 독보적인 성능을 보였습니다.

## 🎯 주요 포인트

- 1. SonicMotion은 FOA 오디오 생성을 위한 최초의 엔드 투 엔드 잠재 확산 프레임워크로, 움직이는 음원에 대한 명시적 제어가 가능합니다.

- 2. SonicMotion은 자연어 프롬프트에 조건을 두는 기술과 텍스트 및 공간 궤적 매개변수에 조건을 두는 기술의 두 가지 변형으로 구현됩니다.

- 3. 새로운 데이터셋은 정적 및 동적 음원과 주석이 달린 방위각, 고도, 운동 속성을 포함한 백만 개 이상의 시뮬레이션된 FOA 캡션 쌍으로 구성됩니다.

- 4. SonicMotion은 최첨단 의미 정렬 및 지각 품질을 달성하며, 특히 낮은 공간 위치 오차를 달성합니다.

---

*Generated on 2025-09-22 14:56:25*