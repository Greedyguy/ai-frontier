# AToken: A Unified Tokenizer for Vision

**Korean Title:** AToken: 비전을 위한 통합 토크나이저

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Unified Visual Tokenization

## 🔗 유사한 논문
- [[2025-09-17/Where Do Tokens Go Understanding Pruning Behaviors in STEP at High Resolutions_20250917|Where Do Tokens Go Understanding Pruning Behaviors in STEP at High Resolutions]] (80.9% similar)
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (80.8% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (80.4% similar)
- [[2025-09-17/Dense Video Understanding with Gated Residual Tokenization_20250917|Dense Video Understanding with Gated Residual Tokenization]] (80.1% similar)
- [[2025-09-19/Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (80.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14476v2 Announce Type: replace-cross 
Abstract: We present AToken, the first unified visual tokenizer that achieves both high-fidelity reconstruction and semantic understanding across images, videos, and 3D assets. Unlike existing tokenizers that specialize in either reconstruction or understanding for single modalities, AToken encodes these diverse visual inputs into a shared 4D latent space, unifying both tasks and modalities in a single framework. Specifically, we introduce a pure transformer architecture with 4D rotary position embeddings to process visual inputs of arbitrary resolutions and temporal durations. To ensure stable training, we introduce an adversarial-free training objective that combines perceptual and Gram matrix losses, achieving state-of-the-art reconstruction quality. By employing a progressive training curriculum, AToken gradually expands from single images, videos, and 3D, and supports both continuous and discrete latent tokens. AToken achieves 0.21 rFID with 82.2% ImageNet accuracy for images, 3.01 rFVD with 40.2% MSRVTT retrieval for videos, and 28.28 PSNR with 90.9% classification accuracy for 3D.. In downstream applications, AToken enables both visual generation tasks (e.g., image generation with continuous and discrete tokens, text-to-video generation, image-to-3D synthesis) and understanding tasks (e.g., multimodal LLMs), achieving competitive performance across all benchmarks. These results shed light on the next-generation multimodal AI systems built upon unified visual tokenization.

## 🔍 Abstract (한글 번역)

arXiv:2509.14476v2 발표 유형: 교체-교차  
초록: 우리는 이미지, 비디오 및 3D 자산 전반에 걸쳐 고충실도 재구성과 의미 이해를 모두 달성하는 최초의 통합 시각 토크나이저인 AToken을 소개합니다. 기존의 토크나이저는 단일 모달리티에 대한 재구성 또는 이해에 특화되어 있는 반면, AToken은 이러한 다양한 시각적 입력을 공유된 4D 잠재 공간으로 인코딩하여 단일 프레임워크에서 두 작업과 모달리티를 통합합니다. 구체적으로, 우리는 임의의 해상도와 시간적 길이를 가진 시각적 입력을 처리하기 위해 4D 회전 위치 임베딩을 갖춘 순수 트랜스포머 아키텍처를 도입합니다. 안정적인 훈련을 보장하기 위해, 우리는 지각적 손실과 Gram 행렬 손실을 결합한 적대적이지 않은 훈련 목표를 도입하여 최첨단 재구성 품질을 달성합니다. 점진적인 훈련 커리큘럼을 사용하여 AToken은 단일 이미지, 비디오 및 3D에서 점차 확장되며, 연속 및 이산 잠재 토큰을 모두 지원합니다. AToken은 이미지에 대해 0.21 rFID와 82.2% ImageNet 정확도를, 비디오에 대해 3.01 rFVD와 40.2% MSRVTT 검색 정확도를, 3D에 대해 28.28 PSNR과 90.9% 분류 정확도를 달성합니다. 다운스트림 응용 프로그램에서 AToken은 시각적 생성 작업(예: 연속 및 이산 토큰을 사용한 이미지 생성, 텍스트-비디오 생성, 이미지-3D 합성)과 이해 작업(예: 다중 모달 LLM)을 가능하게 하여 모든 벤치마크에서 경쟁력 있는 성능을 달성합니다. 이러한 결과는 통합된 시각적 토큰화를 기반으로 구축된 차세대 다중 모달 AI 시스템에 대한 통찰력을 제공합니다.

## 📝 요약

AToken은 이미지, 비디오, 3D 자산에서 고품질 재구성과 의미 이해를 동시에 달성하는 최초의 통합 시각 토크나이저입니다. 기존 토크나이저는 단일 모달리티에 특화되어 있지만, AToken은 4D 잠재 공간에 다양한 시각 입력을 인코딩하여 두 가지 작업과 모달리티를 하나의 프레임워크로 통합합니다. 이를 위해 4D 회전 위치 임베딩을 사용하는 순수 트랜스포머 아키텍처를 도입하여 다양한 해상도와 시간 길이의 시각 입력을 처리합니다. 안정적인 학습을 위해 지각적 손실과 Gram 행렬 손실을 결합한 비대립적 학습 목표를 도입하여 최첨단 재구성 품질을 달성합니다. AToken은 점진적인 학습 커리큘럼을 통해 이미지, 비디오, 3D로 확장하며, 연속 및 이산 잠재 토큰을 지원합니다. 이미지, 비디오, 3D에서 각각 82.2% ImageNet 정확도, 40.2% MSRVTT 검색, 90.9% 분류 정확도를 달성하며, 다양한 벤치마크에서 경쟁력 있는 성능을 보입니다. 이는 통합 시각 토큰화를 기반으로 한 차세대 멀티모달 AI 시스템의 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. AToken은 이미지, 비디오, 3D 자산에 대해 고품질 재구성과 의미 이해를 동시에 달성하는 최초의 통합 비주얼 토크나이저입니다.

- 2. AToken은 다양한 시각 입력을 공유 4D 잠재 공간에 인코딩하여, 단일 프레임워크에서 재구성과 이해 작업을 통합합니다.

- 3. AToken은 순수 트랜스포머 아키텍처와 4D 회전 위치 임베딩을 도입하여 다양한 해상도와 시간 길이의 시각 입력을 처리합니다.

- 4. AToken은 적대적 요소가 없는 학습 목표를 통해 안정적인 학습을 보장하며, 최첨단 재구성 품질을 달성합니다.

- 5. AToken은 이미지, 비디오, 3D의 점진적 학습 커리큘럼을 통해 발전하며, 다양한 다운스트림 응용 프로그램에서 경쟁력 있는 성능을 보입니다.

---

*Generated on 2025-09-22 15:06:07*