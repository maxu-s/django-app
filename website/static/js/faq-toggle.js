document.addEventListener('DOMContentLoaded', function() {
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        const arrow = document.createElement('span');
        arrow.classList.add('arrow');
        arrow.innerHTML = '➔';
        question.appendChild(arrow);

        question.addEventListener('click', function() {
            if (!answer.classList.contains('show')) {
                question.classList.add('expanded');
                answer.classList.add('show');
            } else {
                question.classList.remove('expanded');
                answer.classList.remove('show');
            }
        });
    });
});