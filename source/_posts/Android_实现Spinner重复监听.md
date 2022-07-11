---
title: Android实现Spinner重复监听
date: 2021-03-26 23:44:10
categories: "学习笔记"
tags: Android
---

首先重构Spinner类

```java
import android.content.Context;
import android.util.AttributeSet;
import android.widget.Spinner;

/*
重构spinner以实现点击重复的选项仍然监听
 */

public class ReSpinner extends Spinner {
    public boolean isDropDownMenuShown=false;//标志下拉列表是否正在显示

    public ReSpinner(Context context) {
        super(context);
    }

    public ReSpinner(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    public ReSpinner(Context context, AttributeSet attrs, int defStyle) {
        super(context, attrs, defStyle);
    }

    @Override
    public void
    setSelection(int position, boolean animate) {
        boolean sameSelected = position == getSelectedItemPosition();
        super.setSelection(position, animate);
        if (sameSelected) {
            // 如果选择项是Spinner当前已选择的项,则 OnItemSelectedListener并不会触发,因此这里手动触发回调
            getOnItemSelectedListener().onItemSelected(this, getSelectedView(), position, getSelectedItemId());
        }
    }

    @Override
    public boolean performClick() {
        this.isDropDownMenuShown = true;
        return super.performClick();
    }

    public boolean isDropDownMenuShown(){
        return isDropDownMenuShown;
    }

    public void setDropDownMenuShown(boolean isDropDownMenuShown){
        this.isDropDownMenuShown=isDropDownMenuShown;
    }

    @Override
    public void
    setSelection(int position) {
        boolean sameSelected = position == getSelectedItemPosition();
        super.setSelection(position);
        if (sameSelected) {
            getOnItemSelectedListener().onItemSelected(this, getSelectedView(), position, getSelectedItemId());
        }
    }

    @Override
    public void onDetachedFromWindow() {
        super.onDetachedFromWindow();
    }
}
```

然后将布局文件的标签修改为重构的View类

```xml
<!-- 这里使用了自定义控件的全路径名称 --><com.example.common.util.ReSpinner
      .../>
```
