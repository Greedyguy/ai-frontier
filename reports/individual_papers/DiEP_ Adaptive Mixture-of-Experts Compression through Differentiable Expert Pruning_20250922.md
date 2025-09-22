# DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning

**Korean Title:** DiEP: 미분 가능한 전문가 가지치기를 통한 적응형 전문가 혼합 압축

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/specific/Mixture of Experts|Mixture of Experts]] [[keywords/specific/Gradient Based Pruning|Gradient Based Pruning]] [[keywords/broad/Natural Language Processing|Natural Language Processing]] [[keywords/unique/Differentiable Expert Pruning|Differentiable Expert Pruning]] [[categories/cs.CL|cs.CL]] [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (85.0% similar) [[2025-09-18/Semi-MoE_ Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation_20250918|Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (84.6% similar) [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Mixture of Experts, Gradient Based Pruning
**🔬 Broad Technical**: Natural Language Processing
**⭐ Unique Technical**: Differentiable Expert Pruning
## 🔗 유사한 논문
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (85.0% similar)
- [[2025-09-18/Semi-MoE_ Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation_20250918|Semi-MoE Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (84.6% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (83.7% similar)
- [[2025-09-19/Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (82.5% similar)
- [[2025-09-17/Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection_20250917|Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (82.1% similar)


**ArXiv ID**: [2509.16105](https://arxiv.org/abs/2509.16105)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.16105.pdf)


**ArXiv ID**: [2509.16105](https://arxiv.org/abs/2509.16105)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.16105.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Mixture of Experts, Gradient Based Pruning
**⭐ Unique Technical**: Differentiable Expert Pruning
**🔬 Broad Technical**: Natural Language Processing

## 🏷️ 추출된 키워드



`Natural Language Processing` • 

`Mixture of Experts` • 

`Pruning Strategy` • 

`Differentiable Expert Pruning`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16105v1 Announce Type: new 
Abstract: Despite the significant breakthrough of Mixture-of-Experts (MoE), the increasing scale of these MoE models presents huge memory and storage challenges. Existing MoE pruning methods, which involve reducing parameter size with a uniform sparsity across all layers, often lead to suboptimal outcomes and performance degradation due to varying expert redundancy in different MoE layers. To address this, we propose a non-uniform pruning strategy, dubbed \textbf{Di}fferentiable \textbf{E}xpert \textbf{P}runing (\textbf{DiEP}), which adaptively adjusts pruning rates at the layer level while jointly learning inter-layer importance, effectively capturing the varying redundancy across different MoE layers. By transforming the global discrete search space into a continuous one, our method handles exponentially growing non-uniform expert combinations, enabling adaptive gradient-based pruning. Extensive experiments on five advanced MoE models demonstrate the efficacy of our method across various NLP tasks. Notably, \textbf{DiEP} retains around 92\% of original performance on Mixtral 8$\times$7B with only half the experts, outperforming other pruning methods by up to 7.1\% on the challenging MMLU dataset.

## 🔍 Abstract (한글 번역)

arXiv:2509.16105v1 발표 유형: 신규  
초록: 전문가 혼합(Mixture-of-Experts, MoE)의 상당한 돌파구에도 불구하고, 이러한 MoE 모델의 규모가 커짐에 따라 메모리 및 저장소 문제에 직면하고 있습니다. 모든 층에 걸쳐 균일한 희소성을 적용하여 매개변수 크기를 줄이는 기존의 MoE 가지치기 방법은 다양한 MoE 층에서 전문가의 중복성이 다르기 때문에 최적이 아닌 결과와 성능 저하를 초래하는 경우가 많습니다. 이를 해결하기 위해, 우리는 \textbf{Di}fferentiable \textbf{E}xpert \textbf{P}runing (\textbf{DiEP})이라는 비균일 가지치기 전략을 제안합니다. 이 전략은 층 수준에서 가지치기 비율을 적응적으로 조정하면서 층간 중요성을 공동으로 학습하여, 다양한 MoE 층에서의 중복성을 효과적으로 포착합니다. 전역 이산 탐색 공간을 연속적인 공간으로 변환함으로써, 우리의 방법은 기하급수적으로 증가하는 비균일 전문가 조합을 처리하여 적응적 그래디언트 기반 가지치기를 가능하게 합니다. 다섯 가지 첨단 MoE 모델에 대한 광범위한 실험은 다양한 자연어 처리(NLP) 작업에서 우리의 방법의 효능을 입증합니다. 특히, \textbf{DiEP}는 Mixtral 8$\times$7B에서 전문가 수를 절반으로 줄이면서도 원래 성능의 약 92\%를 유지하며, 도전적인 MMLU 데이터셋에서 다른 가지치기 방법보다 최대 7.1\% 더 우수한 성능을 보입니다.

## 📝 요약

이 논문은 Mixture-of-Experts (MoE) 모델의 메모리 및 저장 문제를 해결하기 위해 비균일 가지치기 전략인 DiEP(Differentiable Expert Pruning)을 제안합니다. 기존의 MoE 가지치기 방법은 모든 층에 균일한 희소성을 적용하여 성능 저하를 초래했으나, DiEP는 층별로 가지치기 비율을 조정하고 층 간 중요도를 학습하여 다양한 중복성을 효과적으로 포착합니다. 이를 통해 전역 이산 탐색 공간을 연속 공간으로 변환하여 적응형 그래디언트 기반 가지치기를 수행합니다. 실험 결과, DiEP는 Mixtral 8×7B 모델에서 절반의 전문가만으로도 원래 성능의 약 92%를 유지하며, MMLU 데이터셋에서 다른 방법보다 최대 7.1% 더 우수한 성능을 보였습니다.

## 🎯 주요 포인트


- 1. Mixture-of-Experts(MoE) 모델의 확장으로 인해 메모리 및 저장 문제 발생.

- 2. 기존 MoE 가지치기 방법은 모든 층에 균일한 희소성을 적용하여 성능 저하 문제를 야기.

- 3. DiEP는 층별로 가지치기 비율을 조정하여 MoE 층 간의 중복성을 효과적으로 포착.

- 4. DiEP는 전역 이산 탐색 공간을 연속 공간으로 변환하여 적응형 그래디언트 기반 가지치기를 가능하게 함.

- 5. DiEP는 Mixtral 8×7B 모델에서 전문가 수를 절반으로 줄이면서도 원래 성능의 약 92%를 유지하며, MMLU 데이터셋에서 최대 7.1% 성능 향상을 달성.


---

*Generated on 2025-09-22 16:29:03*