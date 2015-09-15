var Main = (function() {
    'use strict';

    function MainController() {
        // Not much yet...
    }

    MainController.$inject = [];

    var app = angular.module('app', [])

    .directive('appdata', [function() {
        return {
            bindToController: true,
            controller: MainController,
            controllerAs: 'app'
        };
    }]);
})();