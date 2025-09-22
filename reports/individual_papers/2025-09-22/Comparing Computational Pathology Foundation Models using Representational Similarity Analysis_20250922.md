# Comparing Computational Pathology Foundation Models using Representational Similarity Analysis

**Korean Title:** 컴퓨팅 병리학 기초 모델을 표현 유사성 분석을 통해 비교하기

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision Language Contrastive Learning

## 🔗 유사한 논문
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2 Atypical Mitosis Classification]] (82.7% similar)
- [[2025-09-17/Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation_20250917|Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation]] (79.3% similar)
- [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (78.1% similar)
- [[2025-09-17/PhenoGnet_ A Graph-Based Contrastive Learning Framework for Disease Similarity Prediction_20250917|PhenoGnet A Graph-Based Contrastive Learning Framework for Disease Similarity Prediction]] (78.0% similar)
- [[2025-09-18/Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows_20250918|Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows]] (77.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15482v1 Announce Type: cross 
Abstract: Foundation models are increasingly developed in computational pathology (CPath) given their promise in facilitating many downstream tasks. While recent studies have evaluated task performance across models, less is known about the structure and variability of their learned representations. Here, we systematically analyze the representational spaces of six CPath foundation models using techniques popularized in computational neuroscience. The models analyzed span vision-language contrastive learning (CONCH, PLIP, KEEP) and self-distillation (UNI (v2), Virchow (v2), Prov-GigaPath) approaches. Through representational similarity analysis using H&amp;E image patches from TCGA, we find that UNI2 and Virchow2 have the most distinct representational structures, whereas Prov-Gigapath has the highest average similarity across models. Having the same training paradigm (vision-only vs. vision-language) did not guarantee higher representational similarity. The representations of all models showed a high slide-dependence, but relatively low disease-dependence. Stain normalization decreased slide-dependence for all models by a range of 5.5% (CONCH) to 20.5% (PLIP). In terms of intrinsic dimensionality, vision-language models demonstrated relatively compact representations, compared to the more distributed representations of vision-only models. These findings highlight opportunities to improve robustness to slide-specific features, inform model ensembling strategies, and provide insights into how training paradigms shape model representations. Our framework is extendable across medical imaging domains, where probing the internal representations of foundation models can help ensure effective development and deployment.

## 🔍 Abstract (한글 번역)

arXiv:2509.15482v1 발표 유형: 교차  
초록: 기초 모델은 많은 후속 작업을 촉진할 수 있는 가능성 때문에 계산 병리학(CPath)에서 점점 더 개발되고 있습니다. 최근 연구에서는 모델 간의 작업 성능을 평가했지만, 학습된 표현의 구조와 변동성에 대해서는 잘 알려져 있지 않습니다. 여기에서는 계산 신경과학에서 대중화된 기법을 사용하여 6개의 CPath 기초 모델의 표현 공간을 체계적으로 분석합니다. 분석된 모델은 비전-언어 대조 학습(CONCH, PLIP, KEEP)과 자기 증류(UNI (v2), Virchow (v2), Prov-GigaPath) 접근 방식을 포함합니다. TCGA의 H&E 이미지 패치를 사용한 표현 유사성 분석을 통해, UNI2와 Virchow2가 가장 독특한 표현 구조를 가지고 있는 반면, Prov-Gigapath는 모델 간 평균 유사성이 가장 높다는 것을 발견했습니다. 동일한 훈련 패러다임(비전 전용 대 비전-언어)이 더 높은 표현 유사성을 보장하지는 않았습니다. 모든 모델의 표현은 슬라이드 의존성이 높았지만, 질병 의존성은 상대적으로 낮았습니다. 염색 정규화는 모든 모델에서 슬라이드 의존성을 5.5%(CONCH)에서 20.5%(PLIP)까지 감소시켰습니다. 내재적 차원성 측면에서, 비전-언어 모델은 비전 전용 모델의 더 분산된 표현에 비해 상대적으로 압축된 표현을 보여주었습니다. 이러한 발견은 슬라이드 특정 특징에 대한 강건성을 향상시킬 기회를 강조하고, 모델 앙상블 전략을 안내하며, 훈련 패러다임이 모델 표현을 어떻게 형성하는지에 대한 통찰력을 제공합니다. 우리의 프레임워크는 기초 모델의 내부 표현을 탐색하여 효과적인 개발 및 배포를 보장할 수 있는 의료 영상 도메인 전반에 걸쳐 확장 가능합니다.

## 📝 요약

이 논문은 컴퓨팅 병리학(CPath)에서 사용되는 여섯 가지 기초 모델의 표현 공간을 분석합니다. 연구는 비전-언어 대조 학습(CONCH, PLIP, KEEP)과 자기 증류(UNI (v2), Virchow (v2), Prov-GigaPath) 접근 방식을 포함합니다. H&E 이미지 패치를 사용한 표현 유사성 분석 결과, UNI2와 Virchow2는 가장 독특한 표현 구조를 가지며, Prov-Gigapath는 모델 간 평균 유사성이 가장 높았습니다. 비전-언어 모델은 비교적 압축된 표현을 보였고, 염색 정규화는 모든 모델의 슬라이드 의존성을 감소시켰습니다. 이 연구는 슬라이드 특성에 대한 강인성을 개선하고, 모델 앙상블 전략을 수립하며, 훈련 패러다임이 모델 표현에 미치는 영향을 이해하는 데 기여합니다.

## 🎯 주요 포인트

- 1. 여섯 개의 CPath 기초 모델의 표현 공간을 체계적으로 분석하여 UNI2와 Virchow2가 가장 독특한 표현 구조를 가졌음을 발견했습니다.

- 2. 같은 훈련 패러다임을 공유한다고 해서 더 높은 표현 유사성을 보장하지는 않았습니다.

- 3. 모든 모델의 표현은 슬라이드 의존성이 높았으나, 질병 의존성은 상대적으로 낮았습니다.

- 4. 염색 정규화는 모든 모델에서 슬라이드 의존성을 5.5%에서 20.5%까지 감소시켰습니다.

- 5. 비전-언어 모델은 비전 전용 모델에 비해 상대적으로 압축된 표현을 보여주었습니다.

---

*Generated on 2025-09-22 13:58:58*