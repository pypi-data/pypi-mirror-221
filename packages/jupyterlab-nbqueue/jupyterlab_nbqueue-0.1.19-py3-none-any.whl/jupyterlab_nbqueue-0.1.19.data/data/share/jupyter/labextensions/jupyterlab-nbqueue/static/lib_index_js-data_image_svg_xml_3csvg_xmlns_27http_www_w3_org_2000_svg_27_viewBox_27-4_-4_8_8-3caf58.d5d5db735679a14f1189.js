"use strict";
(self["webpackChunkjupyterlab_nbqueue"] = self["webpackChunkjupyterlab_nbqueue"] || []).push([["lib_index_js-data_image_svg_xml_3csvg_xmlns_27http_www_w3_org_2000_svg_27_viewBox_27-4_-4_8_8-3caf58"],{

/***/ "./lib/components/RunComponent.js":
/*!****************************************!*\
  !*** ./lib/components/RunComponent.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   RunComponent: () => (/* binding */ RunComponent)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_bootstrap_Button__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react-bootstrap/Button */ "./node_modules/react-bootstrap/esm/Button.js");
/* harmony import */ var react_bootstrap_Card__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-bootstrap/Card */ "./node_modules/react-bootstrap/esm/Card.js");
/* harmony import */ var react_bootstrap_Stack__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react-bootstrap/Stack */ "./node_modules/react-bootstrap/esm/Stack.js");
/* harmony import */ var react_bootstrap_OverlayTrigger__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! react-bootstrap/OverlayTrigger */ "./node_modules/react-bootstrap/esm/OverlayTrigger.js");
/* harmony import */ var react_bootstrap_Tooltip__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-bootstrap/Tooltip */ "./node_modules/react-bootstrap/esm/Tooltip.js");
/* harmony import */ var _RunsContext__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./RunsContext */ "./lib/components/RunsContext.js");
/* harmony import */ var _node_modules_bootstrap_dist_css_bootstrap_min_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../node_modules/bootstrap/dist/css/bootstrap.min.css */ "./node_modules/bootstrap/dist/css/bootstrap.min.css");








const RunComponent = ({ run }) => {
    const { deleteRunFromList, getRunsList } = (0,react__WEBPACK_IMPORTED_MODULE_0__.useContext)(_RunsContext__WEBPACK_IMPORTED_MODULE_2__.RunContext);
    const handleDeleteClick = async (event, id, pid) => {
        event.preventDefault();
        deleteRunFromList({ id, pid });
        getRunsList();
    };
    const removeFromListTooltip = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_Tooltip__WEBPACK_IMPORTED_MODULE_3__["default"], { id: "remove-from-list" }, "Remove from list"));
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_Card__WEBPACK_IMPORTED_MODULE_4__["default"], { className: "m-2" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_Card__WEBPACK_IMPORTED_MODULE_4__["default"].Body, null,
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_Stack__WEBPACK_IMPORTED_MODULE_5__["default"], { gap: 1, direction: "horizontal" },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_Stack__WEBPACK_IMPORTED_MODULE_5__["default"], { gap: 1 },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", null, run.name),
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", null, run.status)),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_OverlayTrigger__WEBPACK_IMPORTED_MODULE_6__["default"], { placement: "bottom", overlay: removeFromListTooltip },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_Button__WEBPACK_IMPORTED_MODULE_7__["default"], { className: "ms-auto", variant: "link", size: "sm", onClick: e => handleDeleteClick(e, run.id, run.pid), disabled: false },
                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "fa fa-solid fa-xmark m-2", "aria-hidden": "true" }))))))));
};


/***/ }),

/***/ "./lib/components/RunsContext.js":
/*!***************************************!*\
  !*** ./lib/components/RunsContext.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   RunContext: () => (/* binding */ RunContext),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../handler */ "./lib/handler.js");


const RunContext = react__WEBPACK_IMPORTED_MODULE_0___default().createContext(null);
const RunProvider = ({ children }) => {
    const [runs, setRun] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([]);
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        getRunsList();
    }, []);
    const runObject = async ({ id, pid, name, status, message }) => {
        try {
            await (0,_handler__WEBPACK_IMPORTED_MODULE_1__.requestAPI)('run', {
                method: 'POST',
                body: JSON.stringify({ id, pid, name, status, message })
            });
            getRunsList();
        }
        catch (e) {
            console.log(`There has been an error trying to run an object => ${JSON.stringify(e, null, 2)}`);
        }
    };
    const deleteRunFromList = async ({ id, pid, deleteAll = false }) => {
        try {
            await (0,_handler__WEBPACK_IMPORTED_MODULE_1__.requestAPI)('run', {
                method: 'DELETE',
                body: JSON.stringify({ deleteAll, id, pid })
            });
            getRunsList();
        }
        catch (e) {
            console.log(`There has been an error trying to delete an object from the list of runs => ${e}`);
        }
    };
    let timeoutIteraion = 1;
    const setQueue = (items) => {
        if (items.filter(item => item.status === 'Running').length) {
            setTimeout(() => {
                (async () => {
                    getRunsList();
                })();
            }, 5000 * Math.pow(2, timeoutIteraion - 1));
            timeoutIteraion++;
        }
        else {
            timeoutIteraion = 1;
        }
    };
    const getRunsList = async () => {
        const response = await (0,_handler__WEBPACK_IMPORTED_MODULE_1__.requestAPI)('run');
        setRun(response.reverse());
        timeoutIteraion = 1;
        if (response.filter((item) => item.status === 'Running').length) {
            setQueue(response);
        }
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(RunContext.Provider, { value: {
            runs,
            getRunsList,
            runObject,
            deleteRunFromList
        } }, children));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (RunProvider);


/***/ }),

/***/ "./lib/components/RunsPanelComponent.js":
/*!**********************************************!*\
  !*** ./lib/components/RunsPanelComponent.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   RunsPanelComponent: () => (/* binding */ RunsPanelComponent)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_bootstrap_Stack__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-bootstrap/Stack */ "./node_modules/react-bootstrap/esm/Stack.js");
/* harmony import */ var react_bootstrap_Button__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! react-bootstrap/Button */ "./node_modules/react-bootstrap/esm/Button.js");
/* harmony import */ var react_bootstrap_OverlayTrigger__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react-bootstrap/OverlayTrigger */ "./node_modules/react-bootstrap/esm/OverlayTrigger.js");
/* harmony import */ var react_bootstrap_Tooltip__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-bootstrap/Tooltip */ "./node_modules/react-bootstrap/esm/Tooltip.js");
/* harmony import */ var react_bootstrap_ButtonGroup__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-bootstrap/ButtonGroup */ "./node_modules/react-bootstrap/esm/ButtonGroup.js");
/* harmony import */ var _RunComponent__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./RunComponent */ "./lib/components/RunComponent.js");
/* harmony import */ var _RunsContext__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./RunsContext */ "./lib/components/RunsContext.js");








const RunsPanelComponent = () => {
    const { getRunsList, deleteRunFromList, runs } = (0,react__WEBPACK_IMPORTED_MODULE_0__.useContext)(_RunsContext__WEBPACK_IMPORTED_MODULE_1__.RunContext);
    const handleContextMenuClick = (event) => {
        setTimeout(() => {
            getRunsList();
        }, 1000);
    };
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        window.addEventListener('nbqueueRun', handleContextMenuClick);
        getRunsList();
        return () => {
            window.removeEventListener('nbqueueRun', handleContextMenuClick);
        };
    }, []);
    const handleDelete = (event) => {
        event.preventDefault();
        deleteRunFromList({ deleteAll: true });
        getRunsList();
    };
    const clearListTooltip = react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_Tooltip__WEBPACK_IMPORTED_MODULE_2__["default"], { id: "clear-list" }, "Clear all");
    const refreshTooltip = react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_Tooltip__WEBPACK_IMPORTED_MODULE_2__["default"], { id: "refresh" }, "Refresh");
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { style: {
            display: 'flex',
            flexDirection: 'column',
            height: '100%',
            overflowY: 'auto'
        } },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_Stack__WEBPACK_IMPORTED_MODULE_3__["default"], { gap: 2, direction: "horizontal" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h4", null, "NBQueue history"),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { style: { flex: '1 1 auto' } }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_ButtonGroup__WEBPACK_IMPORTED_MODULE_4__["default"], { className: "p-2", "aria-label": "Runs Utilities" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_OverlayTrigger__WEBPACK_IMPORTED_MODULE_5__["default"], { placement: "bottom", overlay: clearListTooltip },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_Button__WEBPACK_IMPORTED_MODULE_6__["default"], { variant: "link", size: "sm", onClick: e => handleDelete(e), disabled: !!(runs.length === 0) },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("i", { className: "fa fa-solid fa-trash-list m-2 fa-lg", "aria-hidden": "true" }))),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_OverlayTrigger__WEBPACK_IMPORTED_MODULE_5__["default"], { placement: "bottom", overlay: refreshTooltip },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react_bootstrap_Button__WEBPACK_IMPORTED_MODULE_6__["default"], { variant: "link", size: "sm", onClick: getRunsList },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("i", { className: "fa fa-solid fa-arrows-rotate m-2 fa-lg", "aria-hidden": "true" }))))),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null, runs.map(run => {
            return react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_RunComponent__WEBPACK_IMPORTED_MODULE_7__.RunComponent, { key: run.pid, run: run });
        }))));
};


/***/ }),

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   requestAPI: () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'jupyterlab-nbqueue', // API Namespace
    endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.log('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _style_IconsStyle__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./style/IconsStyle */ "./lib/style/IconsStyle.js");
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");
/* harmony import */ var _widgets_RunsPanelWidget__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./widgets/RunsPanelWidget */ "./lib/widgets/RunsPanelWidget.js");





/**
 * Initialization data for the jupyterlab-nbqueue extension.
 */
const plugin = {
    id: 'jupyterlab-nbqueue:plugin',
    description: 'A JupyterLab extension for queuing notebooks executions.',
    autoStart: true,
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0__.IFileBrowserFactory],
    activate: (app, factory) => {
        function urlB64ToUint8Array(base64String) {
            const padding = '='.repeat((4 - (base64String.length % 4)) % 4);
            const base64 = (base64String + padding)
                .replace(/-/g, '+')
                .replace(/_/g, '/');
            const rawData = window.atob(base64);
            const outputArray = new Uint8Array(rawData.length);
            for (let i = 0; i < rawData.length; ++i) {
                outputArray[i] = rawData.charCodeAt(i);
            }
            return outputArray;
        }
        function updateSubscriptionOnServer(subscription) {
            return (0,_handler__WEBPACK_IMPORTED_MODULE_2__.requestAPI)('subscriptions', {
                method: 'POST',
                body: JSON.stringify({
                    subscription_json: JSON.stringify(subscription)
                })
            })
                .then(data => {
                return data;
            })
                .catch(reason => {
                console.error(`${reason}`);
            });
        }
        function subscribeUser(swRegistration, applicationServerPublicKey) {
            const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey);
            swRegistration.pushManager
                .subscribe({
                userVisibleOnly: true,
                applicationServerKey: applicationServerKey
            })
                .then((subscription) => {
                console.log('User is subscribed.');
                return updateSubscriptionOnServer(subscription);
            })
                .then((response) => {
                if (response.status !== 'success') {
                    throw new Error('Bad status code from server.');
                }
                return response;
            })
                .then((responseData) => {
                if (responseData.status !== 'success') {
                    throw new Error('Bad response from server.');
                }
            })
                .catch((err) => {
                console.log('Failed to subscribe the user: ', err);
                console.log(err.stack);
            });
        }
        function registerServiceWorker(serviceWorkerUrl, applicationServerPublicKey) {
            let swRegistration = null;
            if ('serviceWorker' in navigator && 'PushManager' in window) {
                console.log('Service Worker and Push is supported');
                navigator.serviceWorker
                    .register(serviceWorkerUrl)
                    .then(swReg => {
                    console.log('Service Worker is registered');
                    subscribeUser(swReg, applicationServerPublicKey);
                    swRegistration = swReg;
                })
                    .catch(error => {
                    console.error('Service Worker Error', error);
                });
            }
            else {
                console.warn('Push messaging is not supported');
            }
            return swRegistration;
        }
        function askPermission() {
            if (!('serviceWorker' in navigator)) {
                // Service Worker isn't supported on this browser, disable or hide UI.
                alert("Service Worker isn't supported on this browser, disable or hide UI.");
                return;
            }
            if (!('PushManager' in window)) {
                // Push isn't supported on this browser, disable or hide UI.
                alert("Push isn't supported on this browser, disable or hide UI.");
                return;
            }
            return new Promise((resolve, reject) => {
                const permissionResult = Notification.requestPermission(result => {
                    resolve(result);
                });
                if (permissionResult) {
                    permissionResult.then(resolve, reject);
                }
            }).then((permissionResult) => {
                if (permissionResult !== 'granted') {
                    throw new Error("We weren't granted permission.");
                }
                if (permissionResult === 'granted') {
                    registerServiceWorker('http://localhost:8888/files/serviceworker.js', 'BNWsr52JpS-tIoJgJvH_DH7O7DKYDVHLEm1-jJAgQxg92ZMoUjqiElZboqkO8eapp4ZTIv6ZnIiVR_XUU6_CFLk');
                }
            });
        }
        askPermission();
        const runsContent = new _widgets_RunsPanelWidget__WEBPACK_IMPORTED_MODULE_3__.RunsPanelWidget();
        runsContent.addClass('jp-PropertyInspector-placeholderContent');
        const runsWidget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({
            content: runsContent
        });
        runsWidget.toolbar.hide();
        runsWidget.title.icon = _style_IconsStyle__WEBPACK_IMPORTED_MODULE_4__.nbqueueIcon;
        runsWidget.title.caption = 'NBQueue history';
        app.shell.add(runsWidget, 'right', { rank: 501 });
        app.commands.addCommand('jupyterlab-nbqueue:open', {
            label: 'Run',
            caption: "Example context menu button for file browser's items.",
            icon: _style_IconsStyle__WEBPACK_IMPORTED_MODULE_4__.nbqueueIcon,
            execute: () => {
                var _a;
                console.log('jupyterlab-nbqueue:open');
                const file = (_a = factory.tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.selectedItems().next();
                const obj = JSON.parse(JSON.stringify(file));
                if (obj) {
                    (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                        title: obj.name,
                        body: `Notebook ${obj.name} running in background.`,
                        buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton()]
                    }).catch(e => console.log(e));
                }
                (0,_handler__WEBPACK_IMPORTED_MODULE_2__.requestAPI)('run', {
                    method: 'POST',
                    body: JSON.stringify({ notebook: obj.path })
                })
                    .then(data => data)
                    .catch(reason => {
                    console.error(`The jupyterlab-nbqueue server extension appears to be missing.\n${reason}`);
                });
                const event = new Event('nbqueueRun');
                window.dispatchEvent(event);
            }
        });
        app.contextMenu.addItem({
            command: 'jupyterlab-nbqueue:open',
            selector: '.jp-DirListing-item[data-isdir="false"]',
            rank: 0
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/style/IconsStyle.js":
/*!*********************************!*\
  !*** ./lib/style/IconsStyle.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   nbqueueIcon: () => (/* binding */ nbqueueIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _style_nbqueue_logo_v2_svg__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../style/nbqueue_logo_v2.svg */ "./style/nbqueue_logo_v2.svg");


const nbqueueIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({ name: 'nbqueue', svgstr: _style_nbqueue_logo_v2_svg__WEBPACK_IMPORTED_MODULE_1__ });


/***/ }),

/***/ "./lib/widgets/RunsPanelWidget.js":
/*!****************************************!*\
  !*** ./lib/widgets/RunsPanelWidget.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   RunsPanelWidget: () => (/* binding */ RunsPanelWidget)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _components_RunsPanelComponent__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../components/RunsPanelComponent */ "./lib/components/RunsPanelComponent.js");
/* harmony import */ var _components_RunsContext__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../components/RunsContext */ "./lib/components/RunsContext.js");




class RunsPanelWidget extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ReactWidget {
    constructor() {
        super();
    }
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { style: {
                minWidth: '400px',
                display: 'flex',
                flexDirection: 'column',
                background: 'var(--jp-layout-color1)'
            } },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_RunsContext__WEBPACK_IMPORTED_MODULE_2__["default"], null,
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_RunsPanelComponent__WEBPACK_IMPORTED_MODULE_3__.RunsPanelComponent, null))));
    }
}


/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%272%27 fill=%27%23fff%27/%3e%3c/svg%3e":
/*!******************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%272%27 fill=%27%23fff%27/%3e%3c/svg%3e ***!
  \******************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%272%27 fill=%27%23fff%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27%2386b7fe%27/%3e%3c/svg%3e":
/*!*********************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27%2386b7fe%27/%3e%3c/svg%3e ***!
  \*********************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27%2386b7fe%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27%23fff%27/%3e%3c/svg%3e":
/*!******************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27%23fff%27/%3e%3c/svg%3e ***!
  \******************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27%23fff%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27rgba%280, 0, 0, 0.25%29%27/%3e%3c/svg%3e":
/*!***********************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27rgba%280, 0, 0, 0.25%29%27/%3e%3c/svg%3e ***!
  \***********************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27rgba%280, 0, 0, 0.25%29%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27rgba%28255, 255, 255, 0.25%29%27/%3e%3c/svg%3e":
/*!*****************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27rgba%28255, 255, 255, 0.25%29%27/%3e%3c/svg%3e ***!
  \*****************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%27-4 -4 8 8%27%3e%3ccircle r=%273%27 fill=%27rgba%28255, 255, 255, 0.25%29%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 12 12%27 width=%2712%27 height=%2712%27 fill=%27none%27 stroke=%27%23dc3545%27%3e%3ccircle cx=%276%27 cy=%276%27 r=%274.5%27/%3e%3cpath stroke-linejoin=%27round%27 d=%27M5.8 3.6h.4L6 6.5z%27/%3e%3ccircle cx=%276%27 cy=%278.2%27 r=%27.6%27 fill=%27%23dc3545%27 stroke=%27none%27/%3e%3c/svg%3e":
/*!*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 12 12%27 width=%2712%27 height=%2712%27 fill=%27none%27 stroke=%27%23dc3545%27%3e%3ccircle cx=%276%27 cy=%276%27 r=%274.5%27/%3e%3cpath stroke-linejoin=%27round%27 d=%27M5.8 3.6h.4L6 6.5z%27/%3e%3ccircle cx=%276%27 cy=%278.2%27 r=%27.6%27 fill=%27%23dc3545%27 stroke=%27none%27/%3e%3c/svg%3e ***!
  \*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 12 12%27 width=%2712%27 height=%2712%27 fill=%27none%27 stroke=%27%23dc3545%27%3e%3ccircle cx=%276%27 cy=%276%27 r=%274.5%27/%3e%3cpath stroke-linejoin=%27round%27 d=%27M5.8 3.6h.4L6 6.5z%27/%3e%3ccircle cx=%276%27 cy=%278.2%27 r=%27.6%27 fill=%27%23dc3545%27 stroke=%27none%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23000%27%3e%3cpath d=%27M.293.293a1 1 0 0 1 1.414 0L8 6.586 14.293.293a1 1 0 1 1 1.414 1.414L9.414 8l6.293 6.293a1 1 0 0 1-1.414 1.414L8 9.414l-6.293 6.293a1 1 0 0 1-1.414-1.414L6.586 8 .293 1.707a1 1 0 0 1 0-1.414z%27/%3e%3c/svg%3e":
/*!**************************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23000%27%3e%3cpath d=%27M.293.293a1 1 0 0 1 1.414 0L8 6.586 14.293.293a1 1 0 1 1 1.414 1.414L9.414 8l6.293 6.293a1 1 0 0 1-1.414 1.414L8 9.414l-6.293 6.293a1 1 0 0 1-1.414-1.414L6.586 8 .293 1.707a1 1 0 0 1 0-1.414z%27/%3e%3c/svg%3e ***!
  \**************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23000%27%3e%3cpath d=%27M.293.293a1 1 0 0 1 1.414 0L8 6.586 14.293.293a1 1 0 1 1 1.414 1.414L9.414 8l6.293 6.293a1 1 0 0 1-1.414 1.414L8 9.414l-6.293 6.293a1 1 0 0 1-1.414-1.414L6.586 8 .293 1.707a1 1 0 0 1 0-1.414z%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23052c65%27%3e%3cpath fill-rule=%27evenodd%27 d=%27M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e":
/*!****************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23052c65%27%3e%3cpath fill-rule=%27evenodd%27 d=%27M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e ***!
  \****************************************************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23052c65%27%3e%3cpath fill-rule=%27evenodd%27 d=%27M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23212529%27%3e%3cpath fill-rule=%27evenodd%27 d=%27M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e":
/*!****************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23212529%27%3e%3cpath fill-rule=%27evenodd%27 d=%27M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e ***!
  \****************************************************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23212529%27%3e%3cpath fill-rule=%27evenodd%27 d=%27M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%236ea8fe%27%3e%3cpath fill-rule=%27evenodd%27 d=%27M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e":
/*!****************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%236ea8fe%27%3e%3cpath fill-rule=%27evenodd%27 d=%27M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e ***!
  \****************************************************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%236ea8fe%27%3e%3cpath fill-rule=%27evenodd%27 d=%27M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23fff%27%3e%3cpath d=%27M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z%27/%3e%3c/svg%3e":
/*!************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23fff%27%3e%3cpath d=%27M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z%27/%3e%3c/svg%3e ***!
  \************************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23fff%27%3e%3cpath d=%27M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23fff%27%3e%3cpath d=%27M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e":
/*!*************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23fff%27%3e%3cpath d=%27M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e ***!
  \*************************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27 fill=%27%23fff%27%3e%3cpath d=%27M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27%3e%3cpath fill=%27none%27 stroke=%27%23343a40%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%272%27 d=%27m2 5 6 6 6-6%27/%3e%3c/svg%3e":
/*!****************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27%3e%3cpath fill=%27none%27 stroke=%27%23343a40%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%272%27 d=%27m2 5 6 6 6-6%27/%3e%3c/svg%3e ***!
  \****************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27%3e%3cpath fill=%27none%27 stroke=%27%23343a40%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%272%27 d=%27m2 5 6 6 6-6%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27%3e%3cpath fill=%27none%27 stroke=%27%23dee2e6%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%272%27 d=%27m2 5 6 6 6-6%27/%3e%3c/svg%3e":
/*!****************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27%3e%3cpath fill=%27none%27 stroke=%27%23dee2e6%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%272%27 d=%27m2 5 6 6 6-6%27/%3e%3c/svg%3e ***!
  \****************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 16 16%27%3e%3cpath fill=%27none%27 stroke=%27%23dee2e6%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%272%27 d=%27m2 5 6 6 6-6%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 20 20%27%3e%3cpath fill=%27none%27 stroke=%27%23fff%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%273%27 d=%27M6 10h8%27/%3e%3c/svg%3e":
/*!********************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 20 20%27%3e%3cpath fill=%27none%27 stroke=%27%23fff%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%273%27 d=%27M6 10h8%27/%3e%3c/svg%3e ***!
  \********************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 20 20%27%3e%3cpath fill=%27none%27 stroke=%27%23fff%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%273%27 d=%27M6 10h8%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 20 20%27%3e%3cpath fill=%27none%27 stroke=%27%23fff%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%273%27 d=%27m6 10 3 3 6-6%27/%3e%3c/svg%3e":
/*!**************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 20 20%27%3e%3cpath fill=%27none%27 stroke=%27%23fff%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%273%27 d=%27m6 10 3 3 6-6%27/%3e%3c/svg%3e ***!
  \**************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 20 20%27%3e%3cpath fill=%27none%27 stroke=%27%23fff%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%273%27 d=%27m6 10 3 3 6-6%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 30 30%27%3e%3cpath stroke=%27rgba%28255, 255, 255, 0.55%29%27 stroke-linecap=%27round%27 stroke-miterlimit=%2710%27 stroke-width=%272%27 d=%27M4 7h22M4 15h22M4 23h22%27/%3e%3c/svg%3e":
/*!******************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 30 30%27%3e%3cpath stroke=%27rgba%28255, 255, 255, 0.55%29%27 stroke-linecap=%27round%27 stroke-miterlimit=%2710%27 stroke-width=%272%27 d=%27M4 7h22M4 15h22M4 23h22%27/%3e%3c/svg%3e ***!
  \******************************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 30 30%27%3e%3cpath stroke=%27rgba%28255, 255, 255, 0.55%29%27 stroke-linecap=%27round%27 stroke-miterlimit=%2710%27 stroke-width=%272%27 d=%27M4 7h22M4 15h22M4 23h22%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 30 30%27%3e%3cpath stroke=%27rgba%2833, 37, 41, 0.75%29%27 stroke-linecap=%27round%27 stroke-miterlimit=%2710%27 stroke-width=%272%27 d=%27M4 7h22M4 15h22M4 23h22%27/%3e%3c/svg%3e":
/*!***************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 30 30%27%3e%3cpath stroke=%27rgba%2833, 37, 41, 0.75%29%27 stroke-linecap=%27round%27 stroke-miterlimit=%2710%27 stroke-width=%272%27 d=%27M4 7h22M4 15h22M4 23h22%27/%3e%3c/svg%3e ***!
  \***************************************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 30 30%27%3e%3cpath stroke=%27rgba%2833, 37, 41, 0.75%29%27 stroke-linecap=%27round%27 stroke-miterlimit=%2710%27 stroke-width=%272%27 d=%27M4 7h22M4 15h22M4 23h22%27/%3e%3c/svg%3e";

/***/ }),

/***/ "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 8 8%27%3e%3cpath fill=%27%23198754%27 d=%27M2.3 6.73.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z%27/%3e%3c/svg%3e":
/*!**********************************************************************************************************************************************************************************************************************************************************!*\
  !*** data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 8 8%27%3e%3cpath fill=%27%23198754%27 d=%27M2.3 6.73.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z%27/%3e%3c/svg%3e ***!
  \**********************************************************************************************************************************************************************************************************************************************************/
/***/ ((module) => {

module.exports = "data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 8 8%27%3e%3cpath fill=%27%23198754%27 d=%27M2.3 6.73.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z%27/%3e%3c/svg%3e";

/***/ }),

/***/ "./style/nbqueue_logo_v2.svg":
/*!***********************************!*\
  !*** ./style/nbqueue_logo_v2.svg ***!
  \***********************************/
/***/ ((module) => {

module.exports = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Generated by Pixelmator Pro 3.3.6 -->\n<svg width=\"800\" height=\"800\" viewBox=\"0 0 800 800\" xmlns=\"http://www.w3.org/2000/svg\">\n    <g id=\"notebook-svgrepo-com\">\n        <path id=\"Trazado\" fill=\"#69b6a9\" stroke=\"none\" d=\"M 676.253113 127.251587 L 676.253113 742.606262 C 676.253113 774.289063 649.5047 800 616.393738 800 L 59.860939 800 C 58.042187 800 56.225002 799.8703 54.40625 799.740662 C 27.917189 797.403137 6.492188 778.704712 1.16875 754.164063 C 0.65 751.306274 0.259375 748.450012 0.129687 745.46405 C -0 744.554688 -0 743.515625 -0 742.606262 L -0 127.251587 C -0 123.226563 0.389062 119.460938 1.16875 115.695313 C 4.026562 102.710938 11.296875 91.412476 21.554688 83.103149 C 25.190624 80.2453 29.085938 77.648438 33.5 75.701538 C 41.420315 71.935913 50.379688 69.857788 59.859379 69.857788 L 616.392212 69.857788 C 629.117188 69.857788 641.064087 73.623413 650.803162 80.2453 C 655.737488 83.621887 660.15155 87.646851 663.787537 92.190613 C 664.435974 92.970337 665.085938 93.878113 665.734375 94.787476 C 667.553162 97.384399 669.110901 99.981262 670.539063 102.837524 C 671.059387 103.876587 671.578125 104.915649 671.96875 105.954712 C 673.396851 109.459351 674.565613 113.096863 675.215637 116.860962 C 675.474976 118.029663 675.734375 119.198425 675.864075 120.496887 C 676.123413 122.707825 676.253113 124.914063 676.253113 127.251587 Z\"/>\n        <path id=\"path1\" fill=\"#313333\" stroke=\"none\" d=\"M 159.714066 69.859375 L 159.714066 800 L 57.393749 800 C 56.484379 800 55.445313 800 54.535938 799.8703 C 28.046877 798.571899 6.3625 779.354675 1.16875 754.164063 C 0.65 751.306274 0.259375 748.450012 0.129687 745.46405 C 0 744.554688 0 743.515625 0 742.606262 L 0 127.251587 C 0 123.226563 0.389062 119.460938 1.16875 115.695313 C 3.895313 102.320313 11.296875 90.634399 21.554688 82.323425 C 25.320313 79.465637 29.345312 76.868774 33.760937 75.051575 C 39.053123 72.549988 44.940624 71.231262 51.018749 70.546875 C 52.289063 70.367188 53.567188 70.232788 54.862499 70.131226 C 55.721874 70.09375 56.524998 69.857788 57.393749 69.857788 L 159.714066 69.857788 Z\"/>\n        <path id=\"path2\" fill=\"#b2536c\" stroke=\"none\" d=\"M 295.08905 366.078125 L 237.642197 337.581238 L 180.195313 366.078125 L 180.195313 69.868774 L 295.08905 69.868774 Z\"/>\n        <path id=\"path3\" fill=\"#f5e529\" stroke=\"none\" d=\"M 609.865601 33.378113 L 186.943741 33.378113 L 87.414063 33.378113 C 56.546871 33.378113 31.510937 59.104675 31.510937 90.825012 L 31.510937 116.051575 C 31.510937 147.770325 56.546871 173.498413 87.414063 173.498413 L 186.943741 173.498413 L 609.865601 173.498413 C 640.732788 173.498413 665.768738 147.771851 665.768738 116.051575 L 665.768738 90.825012 C 665.768738 59.104675 640.732788 33.378113 609.865601 33.378113 Z\"/>\n        <path id=\"path4\" fill=\"#f2f2f2\" stroke=\"none\" d=\"M 665.768738 98.404663 L 186.943741 98.404663 L 31.510937 98.404663 L 31.510937 745.995361 L 186.943741 745.995361 L 665.768738 745.995361 Z\"/>\n        <linearGradient id=\"linearGradient1\" x1=\"31.510312\" y1=\"742.616719\" x2=\"665.769375\" y2=\"742.616719\" gradientUnits=\"userSpaceOnUse\">\n            <stop offset=\"1e-05\" stop-color=\"#ffffff\" stop-opacity=\"1\"/>\n            <stop offset=\"0.9952\" stop-color=\"#f6f5f5\" stop-opacity=\"1\"/>\n        </linearGradient>\n        <path id=\"path5\" fill=\"url(#linearGradient1)\" stroke=\"none\" d=\"M 634.364075 770.02655 L 53.420311 770.02655 C 41.370312 770.02655 31.509377 760.167175 31.509377 748.115662 L 31.509377 737.117188 C 31.509377 725.0672 41.368752 715.206238 53.420311 715.206238 L 643.857788 715.206238 C 655.907837 715.206238 665.768738 725.065613 665.768738 737.117188 L 665.768738 738.620361 C 665.768738 755.893738 651.637512 770.02655 634.364075 770.02655 Z\"/>\n        <path id=\"path6\" fill=\"#69b6a9\" stroke=\"none\" d=\"M 650.803162 57.523438 L 650.803162 672.748413 C 650.803162 689.628113 643.53125 704.821899 631.974976 715.209412 C 621.846863 724.6875 608.212524 730.271851 593.279724 730.271851 L 57.393749 730.271851 C 49.34375 730.271851 41.81094 728.584351 34.929688 725.596863 C 33.760937 725.206238 32.592186 724.6875 31.554688 724.039063 C 28.048437 722.220337 24.671875 720.143738 21.55625 717.676514 C 21.165625 717.285889 20.646875 717.028137 20.257813 716.637512 C 17.401562 714.170288 14.803125 711.443726 12.467188 708.456238 C 4.675 698.717163 0 686.251526 0 672.748413 L 0 57.523438 C 0 25.709351 25.709375 0 57.393749 0 L 593.279724 0 C 622.885925 0 647.426575 22.46405 650.543762 51.549988 C 650.543762 51.549988 650.543762 51.549988 650.543762 51.679688 C 650.673462 53.628113 650.803162 55.576538 650.803162 57.523438 Z\"/>\n        <path id=\"path7\" fill=\"#d6d7d7\" stroke=\"none\" d=\"M 181.321869 0.032837 L 181.321869 730.226563 L 21.598438 730.226563 L 21.598438 57.478149 C 21.598438 25.757813 47.325001 0.03125 79.045311 0.03125 L 181.321869 0.03125 Z\"/>\n        <path id=\"path8\" fill=\"#505354\" stroke=\"none\" d=\"M 159.714066 0 L 159.714066 730.271851 L 0 730.271851 L 0 57.523438 C 0 25.709351 25.709375 0 57.393749 0 L 159.714066 0 Z\"/>\n        <path id=\"path9\" fill=\"#ebe0ac\" stroke=\"none\" d=\"M 453.770294 194.865601 L 389.565643 160.092163 L 325.360931 194.865601 L 325.360931 0.032837 L 453.770294 0.032837 Z\"/>\n        <path id=\"path10\" fill=\"#bdb595\" stroke=\"none\" d=\"M 418.632782 76.351563 L 396.689056 76.351563 L 394.610931 69.859375 L 389.676575 54.796875 L 389.417206 54.796875 L 384.612488 69.859375 L 382.534393 76.351563 L 360.459381 76.351563 L 360.459381 76.610962 L 378.248444 89.726563 L 375.392212 98.426575 L 371.237488 111.542175 L 371.496857 111.542175 L 389.15625 98.426575 L 389.545319 98.167175 L 389.934387 98.426575 L 407.593719 111.542175 L 407.853119 111.542175 L 403.698456 98.426575 L 400.842194 89.726563 L 418.631256 76.610962 L 418.631256 76.351563 Z\"/>\n        <path id=\"path11\" fill=\"#040000\" stroke=\"none\" opacity=\"0.04\" d=\"M 676.253113 127.251587 L 676.253113 742.606262 C 676.253113 774.289063 649.5047 800 616.393738 800 L 57.393749 800 C 56.484379 800 55.445313 800 54.535938 799.8703 C 28.046877 798.571899 6.3625 779.354675 1.16875 754.164063 C 0.65 751.306274 0.259375 748.450012 0.129687 745.46405 C -0 744.554688 -0 743.515625 -0 742.606262 L -0 720.273438 L 12.465625 708.456238 L 21.554688 699.885925 L 31.553125 690.40625 L 159.714066 569.128113 L 181.268753 548.742188 L 577.957825 173.478149 L 650.803162 104.528137 L 657.165649 98.424988 L 663.787537 92.1922 L 665.734375 90.375 L 665.734375 94.789063 C 667.553162 97.385925 669.110901 99.982788 670.539063 102.83905 C 671.059387 103.878113 671.578125 104.917175 671.96875 105.956238 C 673.396851 109.460938 674.565613 113.09845 675.215637 116.862488 C 675.474976 118.03125 675.734375 119.200012 675.864075 120.498413 C 676.123413 122.707825 676.253113 124.914063 676.253113 127.251587 Z\"/>\n    </g>\n    <g id=\"Circle-icons-gear\">\n        <g id=\"Layer1\">\n            <g id=\"Agrupar\">\n                <path id=\"path12\" fill=\"#76c2af\" stroke=\"none\" d=\"M 589 445 C 589 549.381836 504.381805 634 400 634 C 295.618195 634 211 549.381836 211 445 C 211 340.618195 295.618195 256 400 256 C 504.381805 256 589 340.618195 589 445 Z\"/>\n            </g>\n            <g id=\"g1\" opacity=\"0.2\">\n                <g id=\"g2\">\n                    <path id=\"path13\" fill=\"#231f20\" stroke=\"none\" d=\"M 373.421875 456.8125 C 373.421875 471.578125 385.234375 483.390625 400 483.390625 C 414.765625 483.390625 426.578125 471.578125 426.578125 456.8125 C 426.578125 442.046875 414.765625 430.234375 400 430.234375 C 385.234375 430.234375 373.421875 442.046875 373.421875 456.8125 Z\"/>\n                </g>\n            </g>\n            <g id=\"g3\" opacity=\"0.2\">\n                <path id=\"path14\" fill=\"#231f20\" stroke=\"none\" d=\"M 529.346863 448.543732 C 529.346863 445.590607 526.393738 442.046875 523.440613 440.865631 L 499.225006 432.006256 C 496.271881 430.824982 492.728119 427.28125 491.546875 424.328125 L 487.412506 414.878143 C 486.231232 411.925018 486.231232 407.199982 487.412506 404.246857 L 498.634369 381.212494 C 499.815643 378.259369 499.225006 374.125 497.453125 371.762482 L 485.640625 359.949982 C 483.278107 357.587494 478.553131 356.996857 476.190643 358.768768 L 453.15625 369.990631 C 450.203125 371.171875 445.478119 371.171875 442.524994 369.990631 L 433.074982 365.856232 C 430.121857 364.675018 426.578125 361.131256 425.396881 358.178131 L 416.537506 333.962494 C 415.356232 331.009369 411.8125 328.056244 408.859375 328.056244 C 408.859375 328.056244 405.315643 327.465607 400.590607 327.465607 C 395.865631 327.465607 392.321869 328.056244 392.321869 328.056244 C 389.368744 328.056244 385.825012 331.009369 384.643738 333.962494 L 375.784363 358.178131 C 374.603119 361.131256 371.059387 364.675018 368.106262 365.856232 L 358.65625 369.990631 C 355.703125 371.171875 350.978119 371.171875 348.024994 369.990631 L 324.990631 358.768768 C 322.037506 357.587494 317.903137 358.178131 315.540619 359.949982 L 303.728119 371.762482 C 301.365631 374.125 300.774994 378.850006 302.546875 381.212494 L 313.768738 404.246857 C 314.950012 407.199982 314.950012 411.925018 313.768738 414.878143 L 309.634369 424.328125 C 308.453125 427.28125 304.909363 430.824982 301.956238 432.006256 L 277.740631 440.865631 C 274.787506 442.046875 271.834381 445.590607 271.834381 448.543732 C 271.834381 448.543732 271.243744 452.087494 271.243744 456.8125 C 271.243744 461.537506 271.834381 465.081268 271.834381 465.081268 C 271.834381 468.034393 274.787506 471.578125 277.740631 472.759369 L 301.956238 481.618744 C 304.909363 482.800018 308.453125 486.34375 309.634369 489.296875 L 313.768738 498.746857 C 314.950012 501.699982 314.950012 506.425018 313.768738 509.378143 L 302.546875 532.412476 C 301.365631 535.365601 301.956238 539.5 303.728119 541.862549 L 315.540619 553.674988 C 317.903137 556.037476 322.628113 556.628113 324.990631 554.856262 L 348.024994 543.634399 C 350.978119 542.453125 355.703125 542.453125 358.65625 543.634399 L 368.106262 547.768738 C 371.059387 548.950012 374.603119 552.493774 375.784363 555.446899 L 384.643738 579.662476 C 385.825012 582.615601 389.368744 585.568726 392.321869 585.568726 C 392.321869 585.568726 395.865631 586.159363 400.590607 586.159363 C 405.315643 586.159363 408.859375 585.568726 408.859375 585.568726 C 411.8125 585.568726 415.356232 582.615601 416.537506 579.662476 L 425.396881 555.446899 C 426.578125 552.493774 430.121857 548.950012 433.074982 547.768738 L 442.524994 543.634399 C 445.478119 542.453125 450.203125 542.453125 453.15625 543.634399 L 476.190643 554.856262 C 479.143768 556.037476 483.278107 555.446899 485.640625 553.674988 L 497.453125 541.862549 C 499.815643 539.5 500.40625 534.775024 498.634369 532.412476 L 487.412506 509.378143 C 486.231232 506.425018 486.231232 501.699982 487.412506 498.746857 L 491.546875 489.296875 C 492.728119 486.34375 496.271881 482.800018 499.225006 481.618744 L 523.440613 472.759369 C 526.393738 471.578125 529.346863 468.034393 529.346863 465.081268 C 529.346863 465.081268 529.9375 461.537506 529.9375 456.8125 C 529.9375 452.087494 529.346863 448.543732 529.346863 448.543732 Z M 400 515.875 C 367.515625 515.875 340.9375 489.296875 340.9375 456.8125 C 340.9375 424.328125 367.515625 397.75 400 397.75 C 432.484375 397.75 459.0625 424.328125 459.0625 456.8125 C 459.0625 489.296875 432.484375 515.875 400 515.875 Z\"/>\n            </g>\n            <g id=\"g4\">\n                <g id=\"g5\">\n                    <path id=\"path15\" fill=\"#4f5d73\" stroke=\"none\" d=\"M 373.421875 445 C 373.421875 459.765625 385.234375 471.578125 400 471.578125 C 414.765625 471.578125 426.578125 459.765625 426.578125 445 C 426.578125 430.234375 414.765625 418.421875 400 418.421875 C 385.234375 418.421875 373.421875 430.234375 373.421875 445 Z\"/>\n                </g>\n            </g>\n            <g id=\"g6\">\n                <path id=\"path16\" fill=\"#ffffff\" stroke=\"none\" d=\"M 529.346863 436.731232 C 529.346863 433.778107 526.393738 430.234375 523.440613 429.053131 L 499.225006 420.193756 C 496.271881 419.012482 492.728119 415.46875 491.546875 412.515625 L 487.412506 403.065643 C 486.231232 400.112518 486.231232 395.387482 487.412506 392.434357 L 498.634369 369.399994 C 499.815643 366.446869 499.225006 362.3125 497.453125 359.949982 L 485.640625 348.137482 C 483.278107 345.774994 478.553131 345.184357 476.190643 346.956268 L 453.15625 358.178131 C 450.203125 359.359375 445.478119 359.359375 442.524994 358.178131 L 433.074982 354.043732 C 430.121857 352.862518 426.578125 349.318756 425.396881 346.365631 L 416.537506 322.149994 C 415.356232 319.196869 411.8125 316.243744 408.859375 316.243744 C 408.859375 316.243744 405.315643 315.653107 400.590607 315.653107 C 395.865631 315.653107 392.321869 316.243744 392.321869 316.243744 C 389.368744 316.243744 385.825012 319.196869 384.643738 322.149994 L 375.784363 346.365631 C 374.603119 349.318756 371.059387 352.862518 368.106262 354.043732 L 358.65625 358.178131 C 355.703125 359.359375 350.978119 359.359375 348.024994 358.178131 L 324.990631 346.956268 C 322.037506 345.774994 317.903137 346.365631 315.540619 348.137482 L 303.728119 359.949982 C 301.365631 362.3125 300.774994 367.037506 302.546875 369.399994 L 313.768738 392.434357 C 314.950012 395.387482 314.950012 400.112518 313.768738 403.065643 L 309.634369 412.515625 C 308.453125 415.46875 304.909363 419.012482 301.956238 420.193756 L 277.740631 429.053131 C 274.787506 430.234375 271.834381 433.778107 271.834381 436.731232 C 271.834381 436.731232 271.243744 440.274994 271.243744 445 C 271.243744 449.725006 271.834381 453.268768 271.834381 453.268768 C 271.834381 456.221893 274.787506 459.765625 277.740631 460.946869 L 301.956238 469.806244 C 304.909363 470.987518 308.453125 474.53125 309.634369 477.484375 L 313.768738 486.934357 C 314.950012 489.887482 314.950012 494.612518 313.768738 497.565643 L 302.546875 520.599976 C 301.365631 523.553101 301.956238 527.6875 303.728119 530.050049 L 315.540619 541.862549 C 317.903137 544.224976 322.628113 544.815613 324.990631 543.043701 L 348.024994 531.821899 C 350.978119 530.640625 355.703125 530.640625 358.65625 531.821899 L 368.106262 535.956299 C 371.059387 537.137451 374.603119 540.681274 375.784363 543.634399 L 384.643738 567.849976 C 385.825012 570.803101 389.368744 573.756226 392.321869 573.756226 C 392.321869 573.756226 395.865631 574.346863 400.590607 574.346863 C 405.315643 574.346863 408.859375 573.756226 408.859375 573.756226 C 411.8125 573.756226 415.356232 570.803101 416.537506 567.849976 L 425.396881 543.634399 C 426.578125 540.681274 430.121857 537.137451 433.074982 535.956299 L 442.524994 531.821899 C 445.478119 530.640625 450.203125 530.640625 453.15625 531.821899 L 476.190643 543.043701 C 479.143768 544.224976 483.278107 543.634399 485.640625 541.862549 L 497.453125 530.050049 C 499.815643 527.6875 500.40625 522.962524 498.634369 520.599976 L 487.412506 497.565643 C 486.231232 494.612518 486.231232 489.887482 487.412506 486.934357 L 491.546875 477.484375 C 492.728119 474.53125 496.271881 470.987518 499.225006 469.806244 L 523.440613 460.946869 C 526.393738 459.765625 529.346863 456.221893 529.346863 453.268768 C 529.346863 453.268768 529.9375 449.725006 529.9375 445 C 529.9375 440.274994 529.346863 436.731232 529.346863 436.731232 Z M 400 504.0625 C 367.515625 504.0625 340.9375 477.484375 340.9375 445 C 340.9375 412.515625 367.515625 385.9375 400 385.9375 C 432.484375 385.9375 459.0625 412.515625 459.0625 445 C 459.0625 477.484375 432.484375 504.0625 400 504.0625 Z\"/>\n            </g>\n        </g>\n        <g id=\"Layer2\"/>\n    </g>\n</svg>\n";

/***/ })

}]);
//# sourceMappingURL=lib_index_js-data_image_svg_xml_3csvg_xmlns_27http_www_w3_org_2000_svg_27_viewBox_27-4_-4_8_8-3caf58.d5d5db735679a14f1189.js.map