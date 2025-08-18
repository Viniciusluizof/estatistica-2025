with tb_usuario as (
    SELECT idUsuario, 
    sum(qtdPontos) as qtdPontos
    from points
    GROUP BY idUsuario
),

tb_subset_mediana as(
    SELECT qtdPontos
    from tb_usuario 
    order BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2== 0 from tb_usuario)
    OFFSET (SELECT count(*)/2 from tb_usuario)
),
tb_mediana as (

    SELECT avg(qtdPontos) as Mediana 
    from tb_subset_mediana
),

tb_subset_quartil_01 as(
    SELECT qtdPontos
    from tb_usuario 
    order BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2== 0 from tb_usuario)
    OFFSET (SELECT 1 * count(*)/4 from tb_usuario)
),

tb_quartil_01 as (

    SELECT avg (qtdPontos) as quartil_01
    from tb_subset_quartil_01
    ),

tb_subset_quartil_03 as(
    SELECT qtdPontos
    from tb_usuario 
    order BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2== 0 from tb_usuario)
    OFFSET (SELECT 3 * count(*)/4 from tb_usuario)
),

tb_quartil_03 as (

    SELECT avg (qtdPontos) as quartil_03
    from tb_subset_quartil_01
    ),

tb_stats as (
    SELECT min(qtdPontos) as minimo,
            avg(qtdPontos) as media,
            max(qtdPontos) as maximo
    from tb_usuario
)

SELECT * 
from tb_stats, tb_mediana, tb_quartil_01, tb_quartil_03

