
# Fast Multipole Attention: A Scalable Multilevel Attention Mechanism for Text and Images

**Korean Title:** 패스트 멀티폴 어텐션: 텍스트와 이미지를 위한 확장 가능한 다단계 어텐션 메커니즘

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multilevel Attention

## 🔗 유사한 논문
- [[Superpose_Task-specific_Features_for_Model_Merging_20250919|Superpose Task-specific Features for Model Merging]] (79.2% similar)
- [[MapAnything Universal Feed-Forward Metric 3D Reconstruction]] (78.7% similar)
- [[FAWN A MultiEncoder Fusion-Attention Wave Network for Integrated Sensing and Communication Indoor Scene Inference]] (78.4% similar)
- [[Masked_Feature_Modeling_Enhances_Adaptive_Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (78.3% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (78.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2310.11960v4 Announce Type: replace-cross 
Abstract: While Transformer networks benefit from a global receptive field, their quadratic cost relative to sequence length restricts their application to long sequences and high-resolution inputs. We introduce Fast Multipole Attention (FMA), a divide-and-conquer mechanism for self-attention inspired by the Fast Multipole Method from n-body physics. FMA reduces the time and memory complexity of self-attention from $\mathcal{O}\left(n^2\right)$ to $\mathcal{O}(n \log n)$ and $\mathcal{O}(n)$ while preserving full-context interactions.
  FMA contains a learned hierarchy with $\mathcal{O}(\log n)$ levels of resolution. In this hierarchy, nearby tokens interact at full resolution, while distant tokens engage through progressively coarser, learned basis functions. We have developed both 1D and 2D implementations of FMA for language and vision tasks, respectively. On autoregressive and bidirectional language modeling benchmarks, the 1D variant either matches or outperforms leading efficient attention baselines with substantially lower memory use. With linear complexity, the 2D variant demonstrates superior performance over strong vision transformer baselines in classification and semantic segmentation tasks.
  Our results confirm that the multilevel attention implemented by FMA allows Transformer-based models to scale to much longer sequences and higher-resolution inputs without loss in accuracy. This provides a principled, physics-inspired approach for developing scalable neural networks suitable for language, vision, and multimodal tasks. Our code will be available at https://github.com/epoch98/FMA.

## 🔍 Abstract (한글 번역)

arXiv:2310.11960v4 발표 유형: 교체-교차  
초록: Transformer 네트워크는 전역 수용 영역의 이점을 누리지만, 시퀀스 길이에 따른 이차 비용으로 인해 긴 시퀀스와 고해상도 입력에 대한 적용이 제한됩니다. 우리는 n-체 물리학의 빠른 다중극 방법(Fast Multipole Method)에서 영감을 받은 자기 주의 메커니즘인 빠른 다중극 주의(Fast Multipole Attention, FMA)를 소개합니다. FMA는 자기 주의의 시간 및 메모리 복잡성을 $\mathcal{O}\left(n^2\right)$에서 $\mathcal{O}(n \log n)$ 및 $\mathcal{O}(n)$으로 줄이면서 전체 컨텍스트 상호작용을 유지합니다.  
FMA는 $\mathcal{O}(\log n)$ 수준의 해상도를 가진 학습된 계층 구조를 포함합니다. 이 계층 구조에서, 인접한 토큰은 전체 해상도로 상호작용하며, 먼 토큰은 점진적으로 더 거친 학습된 기저 함수들을 통해 상호작용합니다. 우리는 각각 언어 및 비전 작업을 위한 1D 및 2D FMA 구현을 개발했습니다. 자가회귀 및 양방향 언어 모델링 벤치마크에서, 1D 변형은 메모리 사용량이 상당히 적으면서도 선도적인 효율적 주의 기준선과 동등하거나 더 나은 성능을 보입니다. 선형 복잡성을 가진 2D 변형은 분류 및 의미론적 분할 작업에서 강력한 비전 트랜스포머 기준선을 능가하는 우수한 성능을 보여줍니다.  
우리의 결과는 FMA에 의해 구현된 다중 수준 주의가 트랜스포머 기반 모델이 정확도를 잃지 않고 훨씬 더 긴 시퀀스와 고해상도 입력으로 확장할 수 있게 함을 확인합니다. 이는 언어, 비전 및 다중 모달 작업에 적합한 확장 가능한 신경망을 개발하기 위한 원칙적이고 물리학에 영감을 받은 접근 방식을 제공합니다. 우리의 코드는 https://github.com/epoch98/FMA에서 제공될 예정입니다.

## 📝 요약

이 논문은 긴 시퀀스와 고해상도 입력에 적합한 효율적인 Transformer 네트워크를 제안합니다. 저자들은 n-body 물리학의 Fast Multipole Method에서 영감을 받아 Fast Multipole Attention (FMA)을 개발했습니다. FMA는 시퀀스 길이에 따른 시간 및 메모리 복잡도를 $\mathcal{O}(n^2)$에서 $\mathcal{O}(n \log n)$ 및 $\mathcal{O}(n)$으로 줄이면서도 전체 문맥 상호작용을 유지합니다. FMA는 학습된 계층 구조를 통해 인접 토큰은 높은 해상도로, 먼 토큰은 점진적으로 낮은 해상도로 상호작용합니다. 1D 및 2D 구현을 통해 언어 및 비전 작업에서 기존 모델을 능가하거나 유사한 성능을 보이며, 특히 메모리 사용량이 적습니다. 이 연구는 Transformer 기반 모델이 정확도를 유지하면서 더 긴 시퀀스와 고해상도 입력을 처리할 수 있음을 보여줍니다. 코드는 https://github.com/epoch98/FMA에서 제공됩니다.

## 🎯 주요 포인트

- 1. Fast Multipole Attention (FMA)는 n-body 물리학의 빠른 다중극 방법에서 영감을 받아, 자기 주의 메커니즘의 시간 및 메모리 복잡도를 $\mathcal{O}(n^2)$에서 $\mathcal{O}(n \log n)$ 및 $\mathcal{O}(n)$으로 줄입니다.

- 2. FMA는 학습된 계층 구조를 통해 가까운 토큰은 높은 해상도로, 먼 토큰은 점차 거친 학습 기반 함수로 상호작용합니다.

- 3. 1D FMA는 언어 모델링 벤치마크에서 기존의 효율적인 주의 메커니즘을 메모리 사용량을 줄이면서 성능을 맞추거나 능가합니다.

- 4. 2D FMA는 선형 복잡성을 가지며, 분류 및 의미 분할 작업에서 강력한 비전 트랜스포머 기준보다 우수한 성능을 보입니다.

- 5. FMA는 트랜스포머 기반 모델이 더 긴 시퀀스와 고해상도 입력을 정확도 손실 없이 처리할 수 있도록 하여, 언어, 비전 및 다중 모달 작업에 적합한 확장 가능한 신경망 개발을 위한 물리학에서 영감을 받은 접근 방식을 제공합니다.

---

*Generated on 2025-09-19 15:42:29*