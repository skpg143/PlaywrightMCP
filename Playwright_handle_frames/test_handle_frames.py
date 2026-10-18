from playwright.sync_api import sync_playwright, Page, expect


def test_handle_frames(page: Page):

    page.goto("url")
    frames = page.prames
    print("Number of frame on pages: ", len(frames))
    expect(frames).to_have_count(7)
    page.wait_for_timeout(5000)


    #child frames
    parent_frame = page.frame("url")
    parent_frame.locator("").fill("welcome")
    child_frame = parent_frame.frames
    print("Number of child frame:", len(child_frame))
    page.wait_for_timeout(5000)

    #Inner frames
    inner_frames = child_frame[0]
    radio = inner_frames.get_by_label("I am a human")
    radio.check()
    expect(radio).to_be_checked()
    page.wait_for_timeout(5000)