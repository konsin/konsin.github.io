---
title: EclipseRCP框架
date: 2022-10-24 16:35:08
tags: 
- Java
- RCP框架
categories:
- 学习笔记
---
基于RCP3.x进行学习。
## 基本概念：
1. Display
    应用程序一般只需要一个Display对象，该对象实际是一个SWT对象,代表了底层图形系统的实现。
    Display的主要任务是事件处理，负责从操作系统的时间队列中读取事件，传递给RCP的事件监听器以便完成具体的任务。
    `Display display = new Display()`
2. Shell
    每一个窗口都有一个Shell对象。Shell对象代表了与用户交互的窗口框架，并处理与窗口关联的诸如移动、改变大小等常见行为。
    `Shell shell = new Shell(display);` 或者 `Shell shell = Display.getCurrent().getActiveShell();`
3. Workbench
   Workbench是工作台，代表用户界面的UI元素。有各种窗口、图标、按钮和空间，用户可以在工作台上做各种操作。
   `IWorkbench wb = PlatformUI.getWorkbench();`
   方法：
   - `wb.restart()`，关闭应用程序并立即重新启动。
   - `wb.close()`，正常关闭应用程序。
4. Advisor
    配置用户主界面宽度、高度、图标、菜单、工具栏、颜色、操作等。
    - WorkbenchAdvisor。应用程序级别。每个应用程序只有一个Workbench，WorkbenchAdvisor负责该工作台生命周期的管理，也负责该Workbench的异常处理，并负责向Workbench提供一些重要参数。
    - WorkbenchWindowAdvisor。窗口级别。每一个窗口都有一个WorkbenchWindowAdvisor实例。负责具体窗口生命周期的管理，也可以处理窗口的各种事件例程。
    - ActionBarAdvisor。窗口级别。每一个窗口都有，负责管理窗口菜单栏、状态栏、工具栏的外观和行为。
5. View和Editor
   用户通过视图和编辑器来与程序交互。视图是可以浮动的工作窗口，负责显示。编辑器提供对数据进行各种操作的交互能力。
6. Perspective
   Perspective被称之为透视图，RCP程序通过透视图对窗口内容进行安排和布局，应用程序都有一个默认的透视图，每个工作台窗口则包含一个或多个透视图。透视图需要实现IPerspectiveFactory接口。IPerspectiveFactory可以说是产生初始页面布局和可视性透视图的工厂。
## 生成的类文件分析
1. Application.java
   RCP程序运行开始于Application，Application实现了IPlatformRunnable接口，在RCP启动时将执行start方法。
   ```java
   public class Application implements IApplication {

	@Override
	public Object start(IApplicationContext context) {
		Display display = PlatformUI.createDisplay();
		try {
            //应用程序主窗口只在该句调用之后才会打开并可视化。主窗口启动之后将处于持续打开状态直到用户关闭程序。
            //在打开主窗口之前可以进行用户登录，连接数据库等操作。
			int returnCode = PlatformUI.createAndRunWorkbench(display, new ApplicationWorkbenchAdvisor()); 
			if (returnCode == PlatformUI.RETURN_RESTART) {
				return IApplication.EXIT_RESTART;
			}
			return IApplication.EXIT_OK;
		} finally {
			display.dispose();
		}
	}
   }
   ```

2. 