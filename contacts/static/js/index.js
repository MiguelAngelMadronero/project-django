addEventListener('DOMContentLoaded', ()=>{
    const contadores=document.querySelectorAll('.contador_cantidad');
    const velocidad=1000;

    const animarContadores=()=>{
        for (const contador of contadores) {
            const actualizar_contador=()=>{
                let cantidad_maxima=+contador.dataset.cantidadTotal,
                    valor_actual=+contador.innerText,
                    incremento=cantidad_maxima/velocidad;

                
                if(valor_actual < cantidad_maxima){
                    contador.innerText= Math.ceil( valor_actual + incremento)
                    setTimeout(actualizar_contador, 5)
                    console.log(contador.innerText)
                }else{
                    contador.innerText=cantidad_maxima

                }

            }
            actualizar_contador()
        }
        
    }

    

    const mostrarContadores= elementos=>{
        elementos.forEach(elemento => {
            if (elemento.isIntersecting){
                elemento.target.classList.add('animar');
                elemento.target.classList.remove('ocultar');
                setTimeout(animarContadores, 300)
            }
        });

    }

    //Api para saber cuando algo es visible en el viewport (IntersectionObserver)

    const observer= new IntersectionObserver(mostrarContadores, {
        threshold:0.25 //0 - 1
    })

    const elementosHTML= document.querySelectorAll('.contador_cantidad')
    elementosHTML.forEach(elementoHTML=>{
        observer.observe(elementoHTML)
    })


})


function esVisible(elemento) {
    var rect = elemento.getBoundingClientRect();
    var windowHeight = (window.innerHeight || document.documentElement.clientHeight);
    return !(rect.bottom < 0 || rect.top - windowHeight >= 0);
}

document.addEventListener("scroll", function() {
    var elementos = document.querySelectorAll(".hero__unidad");
    elementos.forEach(function(elemento) {
        if (esVisible(elemento)) {
            elemento.classList.add("animar");
            elemento.classList.remove("ocultar");
        }
    });
});













