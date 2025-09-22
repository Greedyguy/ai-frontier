# RMT-KD: Random Matrix Theoretic Causal Knowledge Distillation

**Korean Title:** RMT-KD: 랜덤 행렬 이론적 인과 지식 증류

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Random Matrix Theory

## 🔗 유사한 논문
- [[2025-09-19/Delta Knowledge Distillation for Large Language Models_20250919|Delta Knowledge Distillation for Large Language Models]] (83.4% similar)
- [[2025-09-19/Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (81.1% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (80.3% similar)
- [[2025-09-19/TableDART_ Dynamic Adaptive Multi-Modal Routing for Table Understanding_20250919|TableDART Dynamic Adaptive Multi-Modal Routing for Table Understanding]] (79.8% similar)
- [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (79.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15724v1 Announce Type: new 
Abstract: Large deep learning models such as BERT and ResNet achieve state-of-the-art performance but are costly to deploy at the edge due to their size and compute demands. We present RMT-KD, a compression method that leverages Random Matrix Theory (RMT) for knowledge distillation to iteratively reduce network size. Instead of pruning or heuristic rank selection, RMT-KD preserves only informative directions identified via the spectral properties of hidden representations. RMT-based causal reduction is applied layer by layer with self-distillation to maintain stability and accuracy. On GLUE, AG News, and CIFAR-10, RMT-KD achieves up to 80% parameter reduction with only 2% accuracy loss, delivering 2.8x faster inference and nearly halved power consumption. These results establish RMT-KD as a mathematically grounded approach to network distillation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15724v1 발표 유형: 신규  
초록: BERT 및 ResNet과 같은 대형 딥러닝 모델은 최첨단 성능을 달성하지만, 그 크기와 연산 요구로 인해 엣지에서의 배포가 비용이 많이 듭니다. 우리는 RMT-KD라는 압축 방법을 제시하며, 이는 랜덤 행렬 이론(RMT)을 활용한 지식 증류를 통해 네트워크 크기를 반복적으로 줄입니다. 가지치기나 휴리스틱 랭크 선택 대신, RMT-KD는 숨겨진 표현의 스펙트럼 특성을 통해 식별된 정보 방향만을 보존합니다. RMT 기반의 인과적 축소는 안정성과 정확성을 유지하기 위해 자기 증류와 함께 계층별로 적용됩니다. GLUE, AG News, CIFAR-10에서 RMT-KD는 최대 80%의 매개변수 감소와 단 2%의 정확도 손실로 2.8배 빠른 추론과 거의 절반의 전력 소비를 달성합니다. 이러한 결과는 RMT-KD를 네트워크 증류에 대한 수학적으로 근거 있는 접근 방식으로 확립합니다.

## 📝 요약

RMT-KD는 대형 딥러닝 모델의 크기와 계산 요구를 줄이기 위해 랜덤 행렬 이론(RMT)을 활용한 지식 증류 방법입니다. 이 방법은 숨겨진 표현의 스펙트럼 특성을 통해 정보가 풍부한 방향만을 보존하여 네트워크 크기를 점진적으로 줄입니다. RMT 기반의 인과적 축소는 각 층에 적용되며, 자기 증류를 통해 안정성과 정확성을 유지합니다. GLUE, AG News, CIFAR-10 데이터셋에서 RMT-KD는 최대 80%의 매개변수 감소와 2%의 정확도 손실만으로 2.8배 빠른 추론과 전력 소비 절반 감소를 달성했습니다. 이는 RMT-KD가 수학적으로 근거 있는 네트워크 증류 방법임을 입증합니다.

## 🎯 주요 포인트

- 1. RMT-KD는 랜덤 행렬 이론을 활용하여 네트워크 크기를 점진적으로 줄이는 지식 증류 방법입니다.

- 2. RMT-KD는 숨겨진 표현의 스펙트럼 특성을 통해 정보가 많은 방향만을 보존하여 네트워크를 압축합니다.

- 3. GLUE, AG News, CIFAR-10 데이터셋에서 최대 80%의 파라미터 감소와 2%의 정확도 손실로 2.8배 빠른 추론을 달성합니다.

- 4. RMT-KD는 수학적으로 근거 있는 네트워크 증류 접근법으로, 전력 소비를 거의 절반으로 줄입니다.

- 5. RMT-KD는 층별 자기 증류를 통해 안정성과 정확성을 유지하면서 인과적 감소를 적용합니다.

---

*Generated on 2025-09-22 15:21:56*