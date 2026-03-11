/*
 * 自定义 JavaScript - 防止左侧导航折叠
 */

document.addEventListener('DOMContentLoaded', function() {
    // 防止导航项点击后自动折叠
    // 监听侧边栏链接点击事件
    var sidebar = document.querySelector('.wy-nav-side');
    if (sidebar) {
        // 防止点击时折叠
        sidebar.addEventListener('click', function(e) {
            // 如果点击的是 toctree-l1 > a 链接，阻止默认行为导致的折叠
            var link = e.target.closest('a');
            if (link && link.parentElement.classList.contains('toctree-l1')) {
                // 延迟执行，确保导航保持展开
                setTimeout(function() {
                    var current = document.querySelector('.toctree-l1.current');
                    if (current) {
                        current.classList.add('toctree-l2'); // 保持展开状态
                    }
                }, 100);
            }
        });
    }

    // 监听导航展开/折叠事件
    var navButtons = document.querySelectorAll('.wy-nav .toggle');
    navButtons.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            // 保持导航展开状态
            var sidebar = document.querySelector('.wy-nav-side');
            if (sidebar) {
                sidebar.classList.remove('wy-collapse');
            }
        });
    });
});
