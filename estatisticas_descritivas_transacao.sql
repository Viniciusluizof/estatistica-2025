WITH tb_subset_mediana as(
    SELECT qtdPontos
    from points 
    order BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2== 0 from points)
    OFFSET (SELECT count(*)/2 from points)
),
tb_mediana as (

    SELECT avg(qtdPontos) as Mediana 
    from tb_subset_mediana
),

tb_subset_quartil_01 as(
    SELECT qtdPontos
    from points 
    order BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2== 0 from points)
    OFFSET (SELECT 1 * count(*)/4 from points)
),

tb_quartil_01 as (

    SELECT avg (qtdPontos) as quartil_01
    from tb_subset_quartil_01
    ),

tb_subset_quartil_03 as(
    SELECT qtdPontos
    from points 
    order BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2== 0 from points)
    OFFSET (SELECT 3 * count(*)/4 from points)
),

tb_quartil_03 as (

    SELECT avg (qtdPontos) as quartil_03
    from tb_subset_quartil_01
    ),

tb_stats as (
    SELECT min(qtdPontos) as minimo,
            avg(qtdPontos) as media,
            max(qtdPontos) as maximo
    FROM points
)

SELECT * 
from tb_stats, tb_mediana, tb_quartil_01, tb_quartil_03