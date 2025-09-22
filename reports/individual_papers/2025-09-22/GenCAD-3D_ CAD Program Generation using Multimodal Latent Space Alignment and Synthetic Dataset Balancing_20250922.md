# GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing

**Korean Title:** GenCAD-3D: 다중 모달 잠재 공간 정렬 및 합성 데이터셋 균형 조정을 통한 CAD 프로그램 생성

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Contrastive Learning, Latent Diffusion Models

## 🔗 유사한 논문
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN Layout-guided 3D Indoor Scene Generation]] (85.0% similar)
- [[2025-09-22/ChannelFlow-Tools_ A Standardized Dataset Creation Pipeline for 3D Obstructed Channel Flows_20250922|ChannelFlow-Tools A Standardized Dataset Creation Pipeline for 3D Obstructed Channel Flows]] (80.0% similar)
- [[2025-09-19/Radiology Report Conditional 3D CT Generation with Multi Encoder Latent diffusion Model_20250919|Radiology Report Conditional 3D CT Generation with Multi Encoder Latent diffusion Model]] (79.5% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (79.4% similar)
- [[2025-09-18/StyleSculptor_ Zero-Shot Style-Controllable 3D Asset Generation with Texture-Geometry Dual Guidance_20250918|StyleSculptor Zero-Shot Style-Controllable 3D Asset Generation with Texture-Geometry Dual Guidance]] (79.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15246v1 Announce Type: cross 
Abstract: CAD programs, structured as parametric sequences of commands that compile into precise 3D geometries, are fundamental to accurate and efficient engineering design processes. Generating these programs from nonparametric data such as point clouds and meshes remains a crucial yet challenging task, typically requiring extensive manual intervention. Current deep generative models aimed at automating CAD generation are significantly limited by imbalanced and insufficiently large datasets, particularly those lacking representation for complex CAD programs. To address this, we introduce GenCAD-3D, a multimodal generative framework utilizing contrastive learning for aligning latent embeddings between CAD and geometric encoders, combined with latent diffusion models for CAD sequence generation and retrieval. Additionally, we present SynthBal, a synthetic data augmentation strategy specifically designed to balance and expand datasets, notably enhancing representation of complex CAD geometries. Our experiments show that SynthBal significantly boosts reconstruction accuracy, reduces the generation of invalid CAD models, and markedly improves performance on high-complexity geometries, surpassing existing benchmarks. These advancements hold substantial implications for streamlining reverse engineering and enhancing automation in engineering design. We will publicly release our datasets and code, including a set of 51 3D-printed and laser-scanned parts on our project site.

## 🔍 Abstract (한글 번역)

arXiv:2509.15246v1 발표 유형: 교차  
초록: CAD 프로그램은 명령어의 매개변수적 시퀀스로 구성되어 정밀한 3D 기하학으로 컴파일되며, 이는 정확하고 효율적인 엔지니어링 설계 과정에 필수적입니다. 포인트 클라우드 및 메쉬와 같은 비매개변수적 데이터로부터 이러한 프로그램을 생성하는 것은 여전히 중요한 과제이며, 일반적으로 광범위한 수작업이 필요합니다. CAD 생성 자동화를 목표로 하는 현재의 심층 생성 모델은 특히 복잡한 CAD 프로그램에 대한 표현이 부족한 불균형하고 충분히 크지 않은 데이터셋으로 인해 상당한 제한을 받고 있습니다. 이를 해결하기 위해, 우리는 CAD 및 기하학 인코더 간의 잠재 임베딩을 정렬하기 위한 대조 학습을 활용하는 다중 모달 생성 프레임워크인 GenCAD-3D를 소개하며, CAD 시퀀스 생성 및 검색을 위한 잠재 확산 모델과 결합하였습니다. 또한, 복잡한 CAD 기하학의 표현을 특히 향상시키기 위해 데이터셋을 균형 있게 확장하도록 설계된 합성 데이터 증강 전략인 SynthBal을 제시합니다. 우리의 실험은 SynthBal이 재구성 정확도를 크게 향상시키고, 잘못된 CAD 모델 생성을 줄이며, 높은 복잡성의 기하학에서 성능을 현저히 개선하여 기존의 벤치마크를 능가함을 보여줍니다. 이러한 발전은 리버스 엔지니어링을 간소화하고 엔지니어링 설계의 자동화를 향상시키는 데 상당한 영향을 미칩니다. 우리는 51개의 3D 프린팅 및 레이저 스캔 부품 세트를 포함한 데이터셋과 코드를 프로젝트 사이트에 공개할 예정입니다.

## 📝 요약

이 논문은 비정형 데이터로부터 CAD 프로그램을 자동 생성하는 데 있어 기존의 한계를 극복하기 위해 GenCAD-3D라는 새로운 생성 프레임워크를 제안합니다. 이 프레임워크는 CAD와 기하학적 인코더 간의 잠재 임베딩을 정렬하는 대조 학습과 CAD 시퀀스 생성 및 검색을 위한 잠재 확산 모델을 결합합니다. 또한, 복잡한 CAD 기하학의 표현을 강화하기 위해 SynthBal이라는 합성 데이터 증강 전략을 도입했습니다. 실험 결과, SynthBal은 복원 정확도를 높이고 잘못된 CAD 모델 생성을 줄이며, 복잡한 기하학에서의 성능을 크게 향상시켰습니다. 이 연구는 역설계 및 엔지니어링 설계 자동화에 중요한 기여를 할 것으로 기대됩니다. 데이터셋과 코드는 프로젝트 사이트에서 공개될 예정입니다.

## 🎯 주요 포인트

- 1. GenCAD-3D는 CAD와 기하학적 인코더 간의 잠재 임베딩을 정렬하기 위해 대조 학습을 활용하는 멀티모달 생성 프레임워크입니다.

- 2. SynthBal은 복잡한 CAD 기하학의 표현을 향상시키기 위해 설계된 합성 데이터 증강 전략으로, 데이터셋의 균형을 맞추고 확장합니다.

- 3. SynthBal을 사용한 실험 결과, 복원 정확도가 크게 향상되고, 잘못된 CAD 모델 생성이 감소하며, 높은 복잡도의 기하학에서 성능이 현저히 개선되었습니다.

- 4. 이러한 발전은 리버스 엔지니어링을 간소화하고 엔지니어링 설계 자동화를 향상시키는 데 중요한 의미를 가집니다.

- 5. 연구팀은 프로젝트 사이트에서 3D 프린팅 및 레이저 스캔된 51개의 부품을 포함한 데이터셋과 코드를 공개할 예정입니다.

---

*Generated on 2025-09-22 13:48:38*