"""A module for testing the ipyvizzu.pyhton.chart module."""

import unittest
import unittest.mock

from tests.chart import (
    TestChartABC,
    TestChartInitABC,
    TestChartMethodsABC,
    TestChartEventsABC,
    TestChartLogsABC,
)
from ipyvizzu.python.chart import Chart


class TestChart(TestChartABC):
    """
    An abstract class for testing Chart() class.
    It is responsible for setup and teardown.
    """

    def get_mock(self):
        return "ipyvizzu.python.chart.Chart._display"

    def get_chart(self, *args, **kwargs):
        return Chart(*args, **kwargs)


class TestChartInit(TestChart, TestChartInitABC, unittest.TestCase):
    """
    A class for testing Chart() class.
    It tests the constructor of the Chart().
    """

    def _assert_equal(self, *args, **kwargs):
        self.assertEqual(*args, **kwargs)

    def _assert_raises(self, *args, **kwargs):
        return self.assertRaises(*args, **kwargs)

    def test_init(
        self,
        reference="window.ipyvizzu.createChart("
        + "document.getElementById(id), "
        + "id, "
        + "'https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js', "
        + "'800px', '480px');",
    ) -> None:
        """A method for testing the default constructor parameters."""

        super().test_init(reference)

    def test_init_vizzu(
        self,
        reference="window.ipyvizzu.createChart("
        + "document.getElementById(id), "
        + "id, "
        + "'https://cdn.jsdelivr.net/npm/vizzu@0.4.1/dist/vizzu.min.js', "
        + "'800px', '480px');",
    ) -> None:
        """A method for testing the "vizzu" constructor parameter."""

        super().test_init_vizzu(reference)

    def test_init_div(
        self,
        reference="window.ipyvizzu.createChart("
        + "document.getElementById(id), "
        + "id, "
        + "'https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js', "
        + "'400px', '240px');",
    ) -> None:
        """A method for testing the "width" and "height" constructor parameters."""

        super().test_init_div(reference)


class TestChartMethods(TestChart, TestChartMethodsABC, unittest.TestCase):
    """
    A class for testing Chart() class.
    It tests ipyvizzu.method-related methods.
    """

    def _assert_equal(self, *args, **kwargs):
        self.assertEqual(*args, **kwargs)

    def _assert_raises(self, *args, **kwargs):
        return self.assertRaises(*args, **kwargs)

    def test_animate_one_chart_target(
        self,
        reference="window.ipyvizzu.animate(document.getElementById(id), id, 'manual', false, "
        + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
        + "undefined);",
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with chart target.
        """

        super().test_animate_one_chart_target(reference)

    def test_animate_one_chart_target_with_chart_anim_opts(
        self,
        reference="window.ipyvizzu.animate(document.getElementById(id), id, 'manual', false, "
        + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
        + '{"duration": "500ms"});',
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with chart target and anim options.
        """

        super().test_animate_one_chart_target_with_chart_anim_opts(reference)

    def test_animate_snapshot_chart_target(
        self,
        reference="window.ipyvizzu.animate(document.getElementById(id), id, 'manual', false, "
        + "id, "
        + "undefined);",
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with Snapshot chart target.
        """

        super().test_animate_snapshot_chart_target(reference)

    def test_animate_snapshot_chart_target_with_chart_anim_opts(
        self,
        reference="window.ipyvizzu.animate(document.getElementById(id), id, 'manual', false, "
        + "id, "
        + '{"duration": "500ms"});',
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with Snapshot chart target and anim options.
        """

        super().test_animate_snapshot_chart_target_with_chart_anim_opts(reference)

    def test_animate_more_chart_target(
        self,
        reference="window.ipyvizzu.animate(document.getElementById(id), id, 'manual', false, "
        + '{"data": {"records": [["Rock", "Hard", 96]]}, '
        + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
        + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
        + "undefined);",
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with multiple chart targets.
        """

        super().test_animate_more_chart_target(reference)

    def test_animate_more_chart_target_with_chart_anim_opts(
        self,
        reference="window.ipyvizzu.animate(document.getElementById(id), id, 'manual', false, "
        + '{"data": {"records": [["Rock", "Hard", 96]]}, '
        + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
        + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
        + '{"duration": "500ms"});',
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with multiple chart targets and anim options.
        """

        super().test_animate_more_chart_target_with_chart_anim_opts(reference)

    def test_animate_more_calls(
        self,
        reference="window.ipyvizzu.animate(document.getElementById(id), id, 'manual', false, "
        + '{"data": {"records": [["Rock", "Hard", 96]]}, '
        + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
        + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
        + "undefined);\n"
        + "window.ipyvizzu.animate(document.getElementById(id), id, 'manual', false, "
        + '{"config": {"title": "Test"}}, '
        + "undefined);",
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests multiple calls.
        """

        super().test_animate_more_calls(reference)

    def test_animate_with_not_default_scroll_into_view(
        self,
        reference="window.ipyvizzu.animate(document.getElementById(id), id, 'manual', {}, "
        + '{{"data": {{"records": [["Rock", "Hard", 96]]}}}}, '
        + "undefined);",
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with "scroll_into_view=True".
        """

        super().test_animate_with_not_default_scroll_into_view(reference)

    def test_feature(
        self,
        reference="window.ipyvizzu.feature(document.getElementById(id), id, 'tooltip', true);",
    ) -> None:
        """A method for testing Chart().feature() method."""

        super().test_feature(reference)

    def test_store(
        self, reference="window.ipyvizzu.store(document.getElementById(id), id, id);"
    ) -> None:
        """A method for testing Chart().store() method."""

        super().test_store(reference)


class TestChartEvents(TestChart, TestChartEventsABC, unittest.TestCase):
    """
    A class for testing Chart() class.
    It tests event-related methods.
    """

    def _assert_equal(self, *args, **kwargs):
        self.assertEqual(*args, **kwargs)

    def _assert_raises(self, *args, **kwargs):
        return self.assertRaises(*args, **kwargs)

    def test_on(
        self,
        reference="window.ipyvizzu.setEvent("
        + "document.getElementById(id), id, id, 'plot-axis-label-draw', "
        + "event => "
        + "{ event.renderingContext.fillStyle = "
        + "(event.data.text === 'Jazz') ? 'red' : 'gray'; });",
    ) -> None:
        """A method for testing Chart().on() method."""

        super().test_on(reference)

    def test_off(
        self,
        reference="window.ipyvizzu.clearEvent(document.getElementById(id), id, id, 'click');",
    ) -> None:
        """A method for testing Chart().off() method."""

        super().test_off(reference)


class TestChartLogs(TestChart, TestChartLogsABC, unittest.TestCase):
    """
    A class for testing Chart() class.
    It tests log-related methods.
    """

    def _assert_equal(self, *args, **kwargs):
        self.assertEqual(*args, **kwargs)

    def _assert_raises(self, *args, **kwargs):
        return self.assertRaises(*args, **kwargs)

    def test_log_config(
        self,
        reference="window.ipyvizzu.log(document.getElementById(id), id, 'config');",
    ) -> None:
        """A method for testing Chart().log() method (ChartProperty.CONFIG)."""

        super().test_log_config(reference)

    def test_log_style(
        self, reference="window.ipyvizzu.log(document.getElementById(id), id, 'style');"
    ) -> None:
        """A method for testing Chart().log() method (ChartProperty.STYLE)."""

        super().test_log_style(reference)
