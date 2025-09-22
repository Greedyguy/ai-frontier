# How many classes do we need to see for novel class discovery?

**Korean Title:** 새로운 클래스 발견을 위해 얼마나 많은 클래스를 보아야 합니까?

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Novel Class Discovery

## 🔗 유사한 논문
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (78.2% similar)
- [[2025-09-19/Data Augmentation via Latent Diffusion Models for Detecting Smell-Related Objects in Historical Artworks_20250919|Data Augmentation via Latent Diffusion Models for Detecting Smell-Related Objects in Historical Artworks]] (77.6% similar)
- [[2025-09-19/MADAR_ Efficient Continual Learning for Malware Analysis with Distribution-Aware Replay_20250919|MADAR Efficient Continual Learning for Malware Analysis with Distribution-Aware Replay]] (77.0% similar)
- [[2025-09-22/Discrete Diffusion in Large Language and Multimodal Models_ A Survey_20250922|Discrete Diffusion in Large Language and Multimodal Models A Survey]] (76.9% similar)
- [[2025-09-22/Pre-Forgettable Models_ Prompt Learning as a Native Mechanism for Unlearning_20250922|Pre-Forgettable Models Prompt Learning as a Native Mechanism for Unlearning]] (76.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15585v1 Announce Type: new 
Abstract: Novel class discovery is essential for ML models to adapt to evolving real-world data, with applications ranging from scientific discovery to robotics. However, these datasets contain complex and entangled factors of variation, making a systematic study of class discovery difficult. As a result, many fundamental questions are yet to be answered on why and when new class discoveries are more likely to be successful. To address this, we propose a simple controlled experimental framework using the dSprites dataset with procedurally generated modifying factors. This allows us to investigate what influences successful class discovery. In particular, we study the relationship between the number of known/unknown classes and discovery performance, as well as the impact of known class 'coverage' on discovering new classes. Our empirical results indicate that the benefit of the number of known classes reaches a saturation point beyond which discovery performance plateaus. The pattern of diminishing return across different settings provides an insight for cost-benefit analysis for practitioners and a starting point for more rigorous future research of class discovery on complex real-world datasets.

## 🔍 Abstract (한글 번역)

arXiv:2509.15585v1 발표 유형: 신규  
초록: 새로운 클래스 발견은 과학적 발견부터 로봇공학에 이르기까지 다양한 응용 분야에서 ML 모델이 변화하는 실제 데이터를 적응하도록 하는 데 필수적입니다. 그러나 이러한 데이터셋은 복잡하고 얽힌 변동 요인을 포함하고 있어 클래스 발견에 대한 체계적인 연구가 어렵습니다. 그 결과, 새로운 클래스 발견이 왜 그리고 언제 더 성공적일 가능성이 높은지에 대한 많은 근본적인 질문들이 아직 답변되지 않았습니다. 이를 해결하기 위해, 우리는 dSprites 데이터셋과 절차적으로 생성된 수정 요인을 사용한 간단한 통제 실험 프레임워크를 제안합니다. 이를 통해 성공적인 클래스 발견에 영향을 미치는 요소를 조사할 수 있습니다. 특히, 알려진/알려지지 않은 클래스의 수와 발견 성과 간의 관계, 그리고 새로운 클래스를 발견하는 데 있어 알려진 클래스의 '커버리지'의 영향을 연구합니다. 우리의 실증적 결과는 알려진 클래스의 수가 증가함에 따라 발견 성과가 포화점에 도달하여 이후에는 성과가 정체되는 현상을 나타냅니다. 다양한 설정에서의 수익 감소 패턴은 실무자들에게 비용-편익 분석에 대한 통찰을 제공하며, 복잡한 실제 데이터셋에서의 클래스 발견에 대한 보다 엄격한 미래 연구의 출발점을 제공합니다.

## 📝 요약

이 논문은 머신러닝 모델이 변화하는 실제 데이터에 적응할 수 있도록 새로운 클래스 발견의 중요성을 다룹니다. 복잡한 데이터셋의 변동 요인으로 인해 체계적인 연구가 어려운 문제를 해결하기 위해, 저자들은 dSprites 데이터셋을 사용한 간단한 실험적 프레임워크를 제안합니다. 이 프레임워크를 통해 알려진 클래스와 미지의 클래스 수가 발견 성능에 미치는 영향과 알려진 클래스의 '커버리지'가 새로운 클래스 발견에 미치는 영향을 연구합니다. 실험 결과, 알려진 클래스 수가 일정 수준을 넘어서면 발견 성능이 정체되는 경향이 나타났습니다. 이는 실무자들에게 비용-효과 분석에 대한 통찰을 제공하며, 복잡한 실제 데이터셋에서의 클래스 발견 연구의 출발점을 제시합니다.

## 🎯 주요 포인트

- 1. 새로운 클래스 발견은 머신러닝 모델이 진화하는 실제 데이터를 적응하는 데 필수적이며, 과학적 발견부터 로봇공학에 이르기까지 다양한 응용 분야가 있다.

- 2. 복잡하고 얽힌 변동 요인을 포함하는 데이터셋은 체계적인 클래스 발견 연구를 어렵게 만든다.

- 3. dSprites 데이터셋을 사용한 간단한 실험적 프레임워크를 제안하여 클래스 발견에 성공적인 영향을 미치는 요인을 조사한다.

- 4. 실험 결과, 알려진 클래스의 수가 일정 수준을 넘어서면 발견 성능이 정체되는 포화점에 도달한다는 것을 보여준다.

- 5. 다양한 설정에서의 수익 감소 패턴은 실무자들에게 비용-편익 분석에 대한 통찰을 제공하고, 복잡한 실제 데이터셋에서 클래스 발견에 대한 향후 연구의 출발점을 제시한다.

---

*Generated on 2025-09-22 15:20:23*