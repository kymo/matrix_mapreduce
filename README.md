# matrix_mapreduce
matrix multiply of map-reduce
大矩阵乘法（C=AB）的map reduce脚本～ 使用稀疏矩阵存储方式，文件matrix中保存的为矩阵tag,行号，列号，元素值。
对于每一行，如果tag为A，则一行A i j Aij生成L个<key value>对，key 为i_k value 为A_j_Aij 
